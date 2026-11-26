from datetime import datetime
import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Smart Plant IoT API", version="0.1.0")

class SensorData(BaseModel):
    soil_moisture: float
    temperature: float
    humidity: float
    light: float

latest = SensorData(soil_moisture=45, temperature=24, humidity=55, light=600)

@app.get("/")
def root():
    return {"name": "Smart Plant IoT", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now().isoformat()}

@app.get("/sensor/latest")
def sensor_latest():
    return latest

@app.get("/sensor/simulate")
def simulate():
    global latest
    latest = SensorData(
        soil_moisture=round(random.uniform(20, 80), 1),
        temperature=round(random.uniform(18, 30), 1),
        humidity=round(random.uniform(35, 80), 1),
        light=round(random.uniform(100, 1000), 1),
    )
    return {**latest.model_dump(), "watering_recommended": latest.soil_moisture < 30}
