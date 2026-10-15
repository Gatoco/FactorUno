"""Unit tests for app.reglas (business rules from HDU_Inacap.xlsx).

Covers Spec S4 (pruebas unitarias, rubric 2.1.6.13): every public and
semipublic function of the module, asserted through its public interface.
"""

import pytest

from app import reglas

COLUMNAS_MONTOS = list(range(8, 20))
COLUMNAS_FACTORES = list(range(8, 38))


class TestRedondear8:
    """redondear_8: ROUND_HALF_UP to the 8th decimal."""

    @pytest.mark.parametrize(
        "valor,esperado",
        [
            (0.123456785, 0.12345679),   # 8th decimal is 8, 9th is 5 -> ties away from zero
            (0.123456784, 0.12345678),   # 9th decimal is 4 -> rounds down
            (1.999999995, 2.0),          # carry propagates through all decimals
            (1 / 3, 0.33333333),         # non-terminating binary float
            (2 / 3, 0.66666667),
        ],
    )
    def test_rounds_half_up_at_eighth_decimal(self, valor, esperado):
        assert reglas.redondear_8(valor) == esperado

    def test_value_already_at_eight_decimals_is_unchanged(self):
        assert reglas.redondear_8(0.12345678) == 0.12345678

    def test_zero_is_preserved(self):
        assert reglas.redondear_8(0.0) == 0.0


class TestCalcularFactores:
    """calcular_factores: factor_i = monto_i / sum(montos 8..19), rounded."""

    def test_all_zero_montos_yield_zero_factors(self):
        factores = reglas.calcular_factores({})
        assert factores == {c: 0.0 for c in COLUMNAS_FACTORES}

    def test_zero_totals_do_not_divide_by_zero(self):
        factores = reglas.calcular_factores({c: 0.0 for c in COLUMNAS_MONTOS})
        assert all(v == 0.0 for v in factores.values())

    def test_all_thirty_columns_8_to_37_are_present(self):
        factores = reglas.calcular_factores({8: 1.0})
        assert set(factores) == set(COLUMNAS_FACTORES)

    def test_normal_case_distributes_each_base_monto_over_total(self):
        # total = 100; expected base factors 0.1 / 0.3 / 0.6
        factores = reglas.calcular_factores({8: 10.0, 9: 30.0, 10: 60.0})
        assert factores[8] == 0.1
        assert factores[9] == 0.3
        assert factores[10] == 0.6

    def test_columns_outside_base_have_zero_factor(self):
        factores = reglas.calcular_factores({8: 10.0, 9: 30.0, 10: 60.0})
        assert all(factores[c] == 0.0 for c in range(11, 20))
        assert all(factores[c] == 0.0 for c in range(20, 38))

    def test_division_result_is_rounded_to_eight_decimals(self):
        factores = reglas.calcular_factores({8: 1.0, 9: 2.0})  # 1/3 and 2/3
        assert factores[8] == 0.33333333
        assert factores[9] == 0.66666667

    @pytest.mark.parametrize(
        "montos",
        [
            {8: 1.0, 9: 2.0},
            {8: 10.0, 9: 30.0, 10: 60.0},
            {c: float(c) for c in COLUMNAS_MONTOS},
        ],
    )
    def test_base_factors_sum_to_one_within_tolerance(self, montos):
        factores = reglas.calcular_factores(montos)
        suma = sum(factores[c] for c in COLUMNAS_MONTOS)
        assert suma == pytest.approx(1.0, abs=1e-8)


class TestValidarSumaFactores:
    """validar_suma_factores: sum of factors 8..19 must be <= 1."""

    def test_sum_exactly_one_passes(self):
        assert reglas.validar_suma_factores({8: 0.5, 9: 0.5}) is None

    def test_single_factor_of_one_passes(self):
        assert reglas.validar_suma_factores({8: 1.0}) is None

    def test_values_inside_tolerance_pass(self):
        # 1.00000001 equals (not exceeds) the threshold -> still accepted
        assert reglas.validar_suma_factores({8: 0.5, 9: 0.50000001}) is None

    def test_columns_above_nineteen_are_ignored(self):
        # only columns 8..19 count, so a large column 30 does not raise
        assert reglas.validar_suma_factores({8: 0.5, 9: 0.5, 30: 99.0}) is None

    def test_missing_columns_default_to_zero(self):
        assert reglas.validar_suma_factores({}) is None

    def test_sum_above_threshold_raises_with_expected_message(self):
        with pytest.raises(ValueError) as exc:
            reglas.validar_suma_factores({8: 2.0})
        assert str(exc.value) == (
            "La suma de los factores de la columna 8 a la 19 es 2.00000000 "
            "y no puede superar 1."
        )

    def test_sum_just_above_threshold_raises(self):
        with pytest.raises(ValueError, match="no puede superar 1"):
            reglas.validar_suma_factores({8: 0.5, 9: 0.50000002})


class TestNormalizarFecha:
    """normalizar_fecha: accept ISO, DD-MM-YYYY and datetime forms -> ISO."""

    @pytest.mark.parametrize(
        "valor,esperado",
        [
            ("2023-12-12", "2023-12-12"),
            ("12-12-2023", "2023-12-12"),
            ("2023-12-12 00:00:00", "2023-12-12"),
            ("12-12-2023 10:30:00", "2023-12-12"),
            ("  2023-12-12  ", "2023-12-12"),
        ],
    )
    def test_recognized_formats_become_iso(self, valor, esperado):
        assert reglas.normalizar_fecha(valor) == esperado

    @pytest.mark.parametrize(
        "valor",
        ["31/12/2023", "2023/12/12", "foo", ""],
    )
    def test_unrecognized_format_raises(self, valor):
        with pytest.raises(ValueError, match="Formato de fecha no reconocido"):
            reglas.normalizar_fecha(valor)


class TestValidarTipoSociedad:
    """_validar_tipo_sociedad: only 'A' or 'C' are accepted."""

    @pytest.mark.parametrize(
        "valor,esperado",
        [
            ("A", "A"),
            ("C", "C"),
            ("a", "A"),
            ("c", "C"),
            ("  c  ", "C"),
            ("\ta\n", "A"),
        ],
    )
    def test_valid_values_are_normalized(self, valor, esperado):
        assert reglas._validar_tipo_sociedad(valor) == esperado

    @pytest.mark.parametrize("valor", ["B", "", "AC", "1"])
    def test_invalid_values_raise(self, valor):
        with pytest.raises(ValueError, match="Tipo sociedad debe ser A o C"):
            reglas._validar_tipo_sociedad(valor)


class TestMapearFilaCsv:
    """mapear_fila_csv: DictReader row -> normalized model dict."""

    @staticmethod
    def _row(**overrides):
        row = {
            "ejercicio": "2023",
            "mercado": "  NYSE ",
            "instrumento": " AAPL ",
            "fecha": "12-12-2023",
            "fecha_pago": "",
            "secuencia": "7",
            "numero_dividendo": "5",
            "tipo_sociedad": " a ",
            "valor_historico": "123.45",
            "isfut": "si",
            "monto_8": "1.5",
            "monto_19": "2.5",
            "factor_8": "0.1",
            "factor_37": "0.25",
        }
        row.update(overrides)
        return row

    def test_maps_scalar_fields_and_normalizes_text(self):
        fila = reglas.mapear_fila_csv(self._row())
        assert fila["ejercicio"] == 2023
        assert fila["mercado"] == "NYSE"
        assert fila["instrumento"] == "AAPL"
        assert fila["secuencia"] == 7
        assert fila["numero_dividendo"] == 5
        assert fila["tipo_sociedad"] == "A"
        assert fila["valor_historico"] == 123.45

    def test_fecha_falls_back_to_fecha_column(self):
        fila = reglas.mapear_fila_csv(self._row(fecha_pago=""))
        assert fila["fecha_pago"] == "2023-12-12"

    @pytest.mark.parametrize("vacio", ["", None])
    def test_empty_fecha_pago_uses_fecha(self, vacio):
        fila = reglas.mapear_fila_csv(self._row(fecha_pago=vacio))
        assert fila["fecha_pago"] == "2023-12-12"

    def test_fecha_pago_takes_precedence_when_present(self):
        fila = reglas.mapear_fila_csv(self._row(fecha_pago="2023-01-02"))
        assert fila["fecha_pago"] == "2023-01-02"

    def test_montos_cover_columns_8_to_19_as_floats(self):
        fila = reglas.mapear_fila_csv(self._row())
        assert set(fila["montos"]) == set(COLUMNAS_MONTOS)
        assert fila["montos"][8] == 1.5
        assert fila["montos"][19] == 2.5
        assert isinstance(fila["montos"][8], float)

    def test_factores_cover_columns_8_to_37_as_floats(self):
        fila = reglas.mapear_fila_csv(self._row())
        assert set(fila["factores"]) == set(COLUMNAS_FACTORES)
        assert fila["factores"][8] == 0.1
        assert fila["factores"][37] == 0.25
        assert isinstance(fila["factores"][8], float)

    def test_missing_monto_and_factor_default_to_zero(self):
        fila = reglas.mapear_fila_csv(self._row())
        assert fila["montos"][9] == 0.0
        assert fila["factores"][9] == 0.0

    @pytest.mark.parametrize("valor", ["1", "TRUE", "S", "SI", "X", "true", " si "])
    def test_isfut_truthy_variants_map_to_one(self, valor):
        fila = reglas.mapear_fila_csv(self._row(isfut=valor))
        assert fila["isfut"] == 1

    @pytest.mark.parametrize("valor", ["0", "NO", "", "false", None])
    def test_isfut_falsy_variants_map_to_zero(self, valor):
        fila = reglas.mapear_fila_csv(self._row(isfut=valor))
        assert fila["isfut"] == 0
