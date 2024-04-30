from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URI de conexión a la base de datos MongoDB desde las variables de entorno
uri = os.getenv("MONGO_URI")

# Crear un nuevo cliente y conectar al servidor de MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Seleccionar la base de datos
db = client["IOT-database"]
# db = client["Base1"]

# Seleccionar la colección de datos de sensores
collection = db["sensors-data"]
# collection = db["Prueba_Servidor"]
