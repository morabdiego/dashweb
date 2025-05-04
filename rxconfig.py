import reflex as rx
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (solo en desarrollo local)
# En Render, las variables se cargan automáticamente desde la configuración del servicio
load_dotenv()

# Obtener API URL desde variables de entorno
api_url = os.getenv("API_URL")

# Verificación de que API_URL está definida
if not api_url:
    raise ValueError("API_URL environment variable is not set. Please define it in your .env file or environment.")

config = rx.Config(
    app_name="dashweb",
    show_built_with_reflex=False,
    # api_url=api_url,
    frontend_port=3000,
    backend_port=8000,
    frontend_path="",
    backend_path="",
    )