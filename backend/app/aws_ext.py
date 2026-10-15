"""Integraciones con almacenamiento no estructurado en AWS (rúbrica 2.1.4.9).

- **DynamoDB**: espejo *best-effort* de los eventos de auditoría, para
  conservar la traza fuera de la base estructurada (SQLite).
- **S3**: exportaciones de respaldo (JSON/CSV) con URL prefirmada temporal.

Ambas integraciones quedan **deshabilitadas** si las variables de entorno no
están definidas, de modo que el desarrollo local y las pruebas no requieren
credenciales de AWS. En el despliegue (EC2 con rol de instancia del Learner
Lab) se configuran FACTORUNO_DYNAMO_TABLA y FACTORUNO_S3_BUCKET.
"""
import os
from datetime import datetime


def _region() -> str:
    return os.environ.get("AWS_REGION", os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))


def tabla_auditoria() -> str:
    return os.environ.get("FACTORUNO_DYNAMO_TABLA", "")


def bucket_exportaciones() -> str:
    return os.environ.get("FACTORUNO_S3_BUCKET", "")


def _cliente_dynamo():
    import boto3
    return boto3.client("dynamodb", region_name=_region())


def _cliente_s3():
    import boto3
    return boto3.client("s3", region_name=_region())


def espejar_auditoria(evento: dict) -> bool:
    """Copia best-effort de un evento de auditoría a DynamoDB.

    Devuelve True si el evento se escribió y False si la integración está
    deshabilitada. Los errores de AWS se absorben: la auditoría local en
    SQLite es la fuente de verdad (base estructurada).
    """
    tabla = tabla_auditoria()
    if not tabla:
        return False
    item = {
        "id": {
            "S": "{fecha}#{accion}#{rid}#{us}".format(
                fecha=evento.get("fecha", ""),
                accion=evento.get("accion", ""),
                rid=evento.get("registro_id", ""),
                us=datetime.now().strftime("%f"),
            )
        },
        "accion": {"S": str(evento.get("accion", ""))},
        "usuario": {"S": str(evento.get("usuario", ""))},
        "detalle": {"S": str(evento.get("detalle", ""))},
        "fecha": {"S": str(evento.get("fecha", ""))},
    }
    if evento.get("registro_id") is not None:
        item["registro_id"] = {"N": str(evento["registro_id"])}
    try:
        _cliente_dynamo().put_item(TableName=tabla, Item=item)
        return True
    except Exception:
        return False


def exportar_a_s3(contenido: str, nombre: str, content_type: str,
                  expira_segundos: int = 3600) -> dict:
    """Sube un respaldo a S3 y devuelve una URL prefirmada temporal.

    Lanza ValueError si S3 no está configurado (la API lo traduce a 503).
    """
    bucket = bucket_exportaciones()
    if not bucket:
        raise ValueError(
            "Almacenamiento S3 no configurado (defina FACTORUNO_S3_BUCKET)"
        )
    cliente = _cliente_s3()
    cliente.put_object(
        Bucket=bucket, Key=nombre, Body=contenido.encode("utf-8"),
        ContentType=content_type,
    )
    url = cliente.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket, "Key": nombre},
        ExpiresIn=expira_segundos,
    )
    return {
        "bucket": bucket,
        "clave": nombre,
        "url_firmada": url,
        "expira_segundos": expira_segundos,
    }
