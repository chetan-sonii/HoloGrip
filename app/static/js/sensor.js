const SENSOR_ENDPOINT = "/api/sensor";
const SENSOR_INTERVAL_MS = 500;

const elements = {
    roll: document.getElementById("roll-value"),
    pitch: document.getElementById("pitch-value"),
    yaw: document.getElementById("yaw-value"),
    temperature: document.getElementById("temperature-value"),
    source: document.getElementById("source-value"),
    timestamp: document.getElementById("timestamp-value"),
    accelX: document.getElementById("accel-x"),
    accelY: document.getElementById("accel-y"),
    accelZ: document.getElementById("accel-z"),
    gyroX: document.getElementById("HoloGrip"),
    gyroY: document.getElementById("gyro-y"),
    gyroZ: document.getElementById("gyro-z"),
    connectionDot: document.getElementById("connection-dot"),
    connectionText: document.getElementById("connection-text"),
};

function setText(element, value) {
    if (element) element.textContent = value;
}

function fixed(value, decimals = 2) {
    return Number(value).toFixed(decimals);
}

function degrees(value) {
    return `${fixed(value, 1)}°`;
}

function updateConnection(connected) {
    if (!elements.connectionDot || !elements.connectionText) return;

    elements.connectionDot.classList.toggle("connected", connected);
    elements.connectionText.textContent = connected ? "Connected" : "Disconnected";
}

function updateDashboard(data) {
    setText(elements.roll, degrees(data.roll));
    setText(elements.pitch, degrees(data.pitch));
    setText(elements.yaw, degrees(data.yaw));

    setText(elements.temperature, `${fixed(data.temperature, 1)}°C`);
    setText(elements.source, data.source);

    setText(elements.accelX, fixed(data.accel_x));
    setText(elements.accelY, fixed(data.accel_y));
    setText(elements.accelZ, fixed(data.accel_z));

    setText(elements.gyroX, fixed(data.gyro_x, 1));
    setText(elements.gyroY, fixed(data.gyro_y, 1));
    setText(elements.gyroZ, fixed(data.gyro_z, 1));

    if (elements.timestamp) {
        elements.timestamp.textContent = new Date(data.timestamp).toLocaleTimeString();
    }

    updateConnection(Boolean(data.connected));

    if (window.gyroScene) {
        window.gyroScene.setOrientation(data.roll, data.pitch, data.yaw);
    }
}

async function fetchSensorData() {
    try {
        const response = await fetch(SENSOR_ENDPOINT, {
            method: "GET",
            headers: { "Accept": "application/json" },
            cache: "no-store",
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const data = await response.json();
        updateDashboard(data);
    } catch (error) {
        console.error("Sensor API request failed:", error);
        updateConnection(false);
    }
}

fetchSensorData();
window.setInterval(fetchSensorData, SENSOR_INTERVAL_MS);
