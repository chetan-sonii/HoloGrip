# HoloGrip — Gyro Sensor Project Website

HoloGrip is a Flask-based project showcase and live sensor demonstration website for an ESP32 + MPU6050 motion-sensing project.

The website is designed specifically for academic evaluation. It explains:

- The problem being addressed
- The proposed solution
- Key features
- Hardware and software technologies
- Technical implementation
- End-to-end data flow
- Live sensor visualization
- Team responsibilities

## Project architecture

```text
ESP32 + MPU6050
       |
       v
Sensor acquisition
       |
       v
Flask API <---- sensor service
       |
       | JSON
       v
Browser AJAX
       |
       v
Dashboard + 3D visualization
```

## Local setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python run.py
```

Open `http://127.0.0.1:5000`.

## Main routes

| Route | Purpose |
|---|---|
| `/` | Main project presentation |
| `/project` | Problem, solution and features |
| `/implementation` | Technical implementation, data flow and technology stack |
| `/demo` | Live sensor dashboard |
| `/team` | Team member presentation |
| `/api/sensor` | Current sensor snapshot as JSON |
| `/api/status` | Connection/status information |
| `/health` | Deployment health endpoint |

## Sensor integration

The current `sensor_service.py` intentionally returns demo data so the website can be developed and evaluated before the real ESP32 communication layer is connected.

The real hardware transport can be added behind the same service interface without changing the presentation routes.

## Deployment

The project contains `render.yaml` for Render deployment. The application uses Gunicorn as its production server.

`APP_URL` is optional and is only used by the project's self-ping worker. Set it to the public application URL when deliberately using that mechanism.
