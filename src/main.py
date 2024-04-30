from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from src.routers import sensordata, sensordata_by_device
from fastapi.middleware.cors import CORSMiddleware

# Creación de la instancia de la aplicación FastAPI
app = FastAPI()

# Configuración de metadatos de la API
app.title = "UdeA - IOT API"  # Título de la API
app.version = "1.0.0"  # Versión de la API

# Configuración de los orígenes permitidos para CORS
origins = [
    "*",  # Permitir todas las fuentes
    "http://localhost",  # Permitir localhost
    "http://localhost:5500",  # Permitir localhost en el puerto 5500
    "http://localhost:5173",  # Permitir localhost en el puerto 5500
]

# Middleware para habilitar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos
    allow_credentials=True,  # Permitir credenciales
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras
)

# Ruta para la página de inicio de la API
@app.get("/", tags=["Home"])
def home():
    return PlainTextResponse("IOT API\nversion:1.0.0\nAuthor:Daniel Estrada\nCopyright 2024")

# Incluir los routers de sensordata y sensordata_by_device
app.include_router(prefix="/sensordata", router=sensordata.router)  # Rutas relacionadas con sensordata
app.include_router(prefix="/sensordata", router=sensordata_by_device.router)  # Rutas relacionadas con sensordata por dispositivo
