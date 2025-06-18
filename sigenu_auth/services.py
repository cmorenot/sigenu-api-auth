import requests
from django.conf import settings

def authenticate_with_aga(username: str, password: str):

    url = settings.AGA_AUTH_URL
    headers = {
        "Origin": f"{settings.ORIGIN_URL}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"AGA {settings.AGA_TOKEN}"
    }
    payload = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)

        print("👉 Código de respuesta:", response.status_code)
        print("👉 Respuesta del AGA:", response.text)

        if response.status_code == 200:
            data = response.json()
            if data.get("OK") and data.get("activeUser", {}).get("account_state") == "TRUE":
                return data["activeUser"]
        return None
    except requests.RequestException as e:
        print("❌ Error de conexión con AGA:", e)
        return None
