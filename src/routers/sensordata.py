from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from ..models.sensordata_model import SensorDataGET, SensorDataPOST, SensorDataGET_justHum, SensorDataGET_justTemp
from ..config.mongo_db import collection
from ..utils.database_utils import filter_db_ordered
from ..utils.commons_parameters import CommonsFilterParams
from starlette.status import HTTP_302_FOUND

router = APIRouter()

# Endpoint para obtener todos los datos de sensores
@router.get("/", tags=["Sensor Data"])
def get_sensordata(kargs: CommonsFilterParams) -> list[SensorDataGET]:
    cursor = collection.find({})  # Obtener todos los documentos de la colección
    data = list(filter_db_ordered(cursor, **kargs))  # Aplicar filtros y ordenar
    for d in data:
        d["_id"] = str(d["_id"])  # Convertir el ID a una cadena
    return data

# Endpoint para agregar nuevos datos de sensores
@router.post("/", tags=["Sensor Data"])
def post_sensordata(new_data: SensorDataPOST):
    inserted_data_id = collection.insert_one(new_data.model_dump()).inserted_id  # Insertar datos en la colección
    return RedirectResponse(f"/sensordata/{inserted_data_id}", status_code=HTTP_302_FOUND)  # Redirigir a la URL del nuevo documento

# Endpoint para obtener el dato más reciente de sensores
@router.get("/lastest", tags=["Sensor Data"])
def get_lastest_sensordata() -> SensorDataGET:
    data = list(filter_db_ordered(collection.find({}), limit=1))[0]  # Obtener el dato más reciente y convertir el ID
    data["_id"] = str(data["_id"])
    return data

# Endpoint para obtener datos de sensores solo con temperatura
@router.get("/temp", tags=["Sensor Data"])
def get_sensordata_by_temp(kargs: CommonsFilterParams) -> list[SensorDataGET_justTemp]:
    cursor = collection.find({}, {"device":1, "temperature": 1, "date": 1})  # Obtener solo los campos necesarios
    data = list(filter_db_ordered(cursor, **kargs))  # Aplicar filtros y ordenar
    for d in data:
        d["_id"] = str(d["_id"])  # Convertir el ID a una cadena
    return data

# Endpoint para obtener datos de sensores solo con humedad
@router.get("/hum", tags=["Sensor Data"])
def get_sensordata_by_hum(kargs: CommonsFilterParams) -> list[SensorDataGET_justHum]:
    cursor = collection.find({}, {"device":1, "humidity": 1, "date": 1})  # Obtener solo los campos necesarios
    data = list(filter_db_ordered(cursor, **kargs))  # Aplicar filtros y ordenar
    for d in data:
        d["_id"] = str(d["_id"])  # Convertir el ID a una cadena
    return data
