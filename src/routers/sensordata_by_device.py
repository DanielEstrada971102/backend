from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, RedirectResponse
from src.models.sensordata_model import SensorDataGET_byD, deviceName, SensorDataGET_justHum_byD, SensorDataGET_justTemp_byD
from ..config.mongo_db import collection
from ..utils.database_utils import filter_db_ordered
from ..utils.commons_parameters import CommonsFilterParams
from starlette.status import HTTP_302_FOUND

router = APIRouter()

# Obtener datos de sensores por dispositivo
@router.get("/{device}", tags=["Sensor data by device"])
def get_sensordata(device: deviceName, kargs: CommonsFilterParams) -> list[SensorDataGET_byD]:
    cursor = collection.find({"device": device})  # Filtrar datos por dispositivo
    data = list(filter_db_ordered(cursor, **kargs))  # Aplicar filtros y ordenar
    for d in data:
        d["_id"] = str(d["_id"])  # Convertir el ID a una cadena
    return data

# Obtener el dato más reciente de un dispositivo
@router.get("/{device}/lastest", tags=["Sensor data by device"])
def get_sensordata(device: deviceName)-> SensorDataGET_byD:
    data = list(filter_db_ordered(collection.find({"device": device}), limit=1))[0]  # Obtener el dato más reciente
    data["_id"] = str(data["_id"])  # Convertir el ID a una cadena
    return data

# Obtener datos de sensores de temperatura por dispositivo
@router.get("/{device}/temp", tags=["Sensor data by device"])
def get_sensordata(device: deviceName, kargs: CommonsFilterParams)-> list[SensorDataGET_justTemp_byD]:
    cursor = collection.find({"device": device}, {"temperature": 1, "date": 1})  # Filtrar solo temperatura y fecha
    data = list(filter_db_ordered(cursor, **kargs))  # Aplicar filtros y ordenar
    for d in data:
        d["_id"] = str(d["_id"])  # Convertir el ID a una cadena
    return data

# Obtener datos de sensores de humedad por dispositivo
@router.get("/{device}/hum", tags=["Sensor data by device"])
def get_sensordata(device: deviceName, kargs: CommonsFilterParams) -> list[SensorDataGET_justHum_byD]:
    cursor = collection.find({"device": device}, {"humidity": 1, "date": 1})  # Filtrar solo humedad y fecha
    data = list(filter_db_ordered(cursor, **kargs))  # Aplicar filtros y ordenar
    for d in data:
        d["_id"] = str(d["_id"])  # Convertir el ID a una cadena
    return data
