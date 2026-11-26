# Smart Plant IoT

A portfolio-oriented IoT project combining embedded development, Python APIs, data storage and automated plant watering.

## v0.1 features

- FastAPI backend
- Health-check endpoint
- Simulated soil moisture, temperature, humidity and light data
- Simple watering recommendation (`soil_moisture < 30`)
- ESP32 firmware placeholder for the next phase

## Project structure

```text
smart-plant-iot/
├── backend/
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── firmware/
│   └── esp32/
│       └── README.md
├── docs/
├── .gitignore
└── README.md
```

## Run locally on Windows

Open CMD or PowerShell in the project root.

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r backend\requirements.txt
python -m uvicorn backend.app.main:app --reload
```

Then open:

- API: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- Simulated data: http://127.0.0.1:8000/sensor/simulate

## First push to GitHub

If you downloaded this project as ZIP and want to upload it into an already-created repository, copy these files into your cloned repository, then run:

```cmd
git status
git add .
git commit -m "Add initial Smart Plant IoT backend"
git push
```

## Roadmap

1. PostgreSQL sensor history
2. MQTT communication
3. ESP32 sensor acquisition
4. Automatic pump control
5. Web dashboard and charts
6. Docker Compose
7. Alerts and watering strategy
