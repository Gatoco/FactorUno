const API = '/api'

const TOKEN_KEY = 'factoruno_token'
const USER_KEY = 'factoruno_usuario'

export function getToken() {
  return localStorage.getItem(TOKEN_KEY)
}

export function guardarSesion(data) {
  localStorage.setItem(TOKEN_KEY, data.access_token)
  localStorage.setItem(USER_KEY, JSON.stringify({ usuario: data.usuario, rol: data.rol }))
}

export function limpiarSesion() {
  localStorage.removeItem(TOKEN_KEY)
  localStorage.removeItem(USER_KEY)
}

function manejar401(res) {
  if (res.status === 401 && getToken()) {
    limpiarSesion()
    window.dispatchEvent(new Event('sesion-expirada'))
  }
}

async function request(path, options = {}) {
  const token = getToken()
  const res = await fetch(API + path, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
  })
  manejar401(res)
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error(body.detail || `Error ${res.status}`)
  }
  if (res.status === 204) return null
  return res.json()
}

export const api = {
  login: (usuario, password) =>
    request('/auth/login', { method: 'POST', body: JSON.stringify({ usuario, password }) }),
  me: () => request('/auth/me'),
  listar: (filtros) => {
    const q = new URLSearchParams()
    if (filtros.mercado) q.set('mercado', filtros.mercado)
    if (filtros.origen) q.set('origen', filtros.origen)
    if (filtros.periodo) q.set('periodo', filtros.periodo)
    const s = q.toString()
    return request('/calificaciones' + (s ? `?${s}` : ''))
  },
  obtener: (id) => request(`/calificaciones/${id}`),
  crear: (data) => request('/calificaciones', { method: 'POST', body: JSON.stringify(data) }),
  modificar: (id, data) => request(`/calificaciones/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  eliminar: (id) => request(`/calificaciones/${id}`, { method: 'DELETE' }),
  calcular: (id) => request(`/calificaciones/${id}/calcular`, { method: 'POST' }),
  auditoria: () => request('/auditoria'),
  exportar: (formato) => request(`/exportar?formato=${formato}`),
  cargar: async (archivo, tipo) => {
    const fd = new FormData()
    fd.append('archivo', archivo)
    const token = getToken()
    const res = await fetch(`${API}/carga?tipo=${tipo}`, {
      method: 'POST',
      body: fd,
      headers: token ? { Authorization: `Bearer ${token}` } : {},
    })
    manejar401(res)
    if (!res.ok) {
      const body = await res.json().catch(() => ({}))
      throw new Error(body.detail || `Error ${res.status}`)
    }
    return res.json()
  },
}
