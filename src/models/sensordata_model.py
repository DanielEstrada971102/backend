from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

# Definición de una enumeración para los nombres de los dispositivos
class deviceName(str, Enum):
    arduino = "arduino"
    esp32 = "esp32"


# Definición del modelo para obtener datos de sensores
class SensorDataGET(BaseModel):
    id: str  = Field(alias="_id")
    device: deviceName 
    temperature: float
    humidity: float
    date: str


# Definición del modelo para obtener datos de sensores filtrados por dispositivo
class SensorDataGET_byD(BaseModel):
    id: str  = Field(alias="_id")
    temperature: float
    humidity: float
    date: str


# Definición del modelo para obtener solo la temperatura de los datos de sensores
class SensorDataGET_justTemp(BaseModel):
    id: str  = Field(alias="_id")
    device: Optional[deviceName] = deviceName.arduino
    temperature: float
    date: str


# Definición del modelo para obtener solo la temperatura de los datos de sensores filtrados por dispositivo
class SensorDataGET_justTemp_byD(BaseModel):
    id: str  = Field(alias="_id")
    temperature: float
    date: str


# Definición del modelo para obtener solo la humedad de los datos de sensores
class SensorDataGET_justHum(BaseModel):
    id: str  = Field(alias="_id")
    device: Optional[deviceName] = deviceName.arduino
    humidity: float
    date: str   


# Definición del modelo para obtener solo la humedad de los datos de sensores filtrados por dispositivo
class SensorDataGET_justHum_byD(BaseModel):
    id: str  = Field(alias="_id")
    humidity: float
    date: str


# Definición del modelo para enviar datos de sensores
class SensorDataPOST(BaseModel):
    device: deviceName 
    temperature: float
    humidity: float
    date: Optional[str] = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M-%S")) 