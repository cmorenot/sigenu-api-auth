# SIGENU Auth API

Proyecto Django REST Framework para autenticación externa contra el sistema AGA (API LDAP de la Universidad de Holguín), compatible con la integración de SIGENU mediante servicios REST seguros.

---

## 🔐 Funcionalidad

Este servicio REST:

- Recibe credenciales (`username`, `password`) desde SIGENU u otro cliente externo.
- Llama a la API LDAP institucional (AGA_AUTH) para validar autenticidad.
- Retorna los datos del usuario en el formato exacto que SIGENU espera.
- Rechaza el acceso si el usuario no existe, está inactivo o las credenciales son incorrectas.

---

## ⚙️ Tecnologías utilizadas

- Python 3.10+
- Django 5.2+
- Django REST Framework
- django-environ
- requests

---

## 🚀 Instalación y configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/sigenu_auth.git
cd sigenu_auth


python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt


SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

AGA_AUTH_URL=https://api.ldap.uho.edu.cu/login
AGA_TOKEN=tu_token_autenticacion_aga


curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"usuario\", \"password\": \"contraseña\"}"


http://127.0.0.1:8000/api/auth/login/


{
  "email": "",
  "facultyId": null,
  "townUniversityId": null,
  "identification": "12345678900",
  "lastname": "SegundoApellido",
  "name": "Carlos",
  "role": "STUDENT",
  "status": "ACTIVE",
  "surname": "PrimerApellido",
  "username": "cmorenot"
}
