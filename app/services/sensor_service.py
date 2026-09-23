from datetime import datetime, timezone


# Demo data for development and website evaluation.
# This service is the intended replacement point for the real ESP32 transport layer.


def get_sensor_snapshot():
    return {
        "connected": True,
        "source": "demo",
        "roll": 12.4,
        "pitch": -4.2,
        "yaw": 87.6,
        "accel_x": 0.12,
        "accel_y": -0.03,
        "accel_z": 0.98,
        "gyro_x": 1.4,
        "gyro_y": -0.7,
        "gyro_z": 0.9,
        "temperature": 28.4,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
