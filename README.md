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
```

### 2. Crea el entorno virtual e instálalo

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

### 3. Crea el archivo `.env` en la raíz

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

AGA_AUTH_URL=https://api.ldap.uho.edu.cu/login
AGA_TOKEN=tu_token_autenticacion_aga
```

### 4. Migraciones y ejecución del servidor

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Pruebas

Puedes hacer una prueba desde `curl`, Postman o desde el navegador:

### Ejemplo con `curl`:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"usuario\", \"password\": \"contraseña\"}"
```

O visita en el navegador:

```
http://127.0.0.1:8000/api/auth/login/
```

Y prueba desde la interfaz de Django REST Framework.

---

## 📥 Respuesta esperada (formato SIGENU)

```json
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
```

---

## 🔒 Seguridad

- Las variables sensibles se gestionan vía `.env` usando `django-environ`.
- Los headers del API LDAP están protegidos con autenticación tipo `Authorization: AGA <token>`.
- Manejo de errores robusto en la conexión con servicios externos.
- No se expone información interna en respuestas de error.

---

## 🧑‍💻 Autor

- **Carlos Moreno** – [cmorenot@uho.edu.cu]

---

## 📄 Licencia

Este proyecto es de uso universitario y puede adaptarse con fines educativos o institucionales.
