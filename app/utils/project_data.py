PROJECT = {
    "name": "HoloGrip",
    "tagline": "Motion sensing transformed into interactive digital control.",
    "short_description": (
        "A compact embedded-system project that uses an MPU6050 motion sensor "
        "with an ESP32 to capture movement data and visualize orientation in real time."
    ),
    "problem": (
        "Traditional computer input devices are built around clicks, keys and fixed controls. "
        "They do not naturally capture the physical orientation and movement of a handheld object. "
        "This creates an opportunity to explore motion as a direct input method."
    ),
    "youtube_url": "https://youtube.com/shorts/zf-vR_R6oDQ?si=NHeCUxck_l5Kujs4",
    "github_url": "https://github.com/chetan-sonii/HoloGrip.git",
    "solution": (
        "HoloGrip combines an MPU6050 inertial sensor with an ESP32. The sensor measures "
        "acceleration and angular velocity, the ESP32 acquires the readings, and the software "
        "pipeline converts the data into live values that can be visualized and used for interaction."
    ),
}

FEATURES = [
    {
        "icon": "bi-activity",
        "title": "Real-Time Motion Data",
        "text": "Sensor readings are displayed continuously so movement can be observed as it happens.",
    },
    {
        "icon": "bi-compass",
        "title": "3-Axis Orientation",
        "text": "Roll, pitch and yaw provide an intuitive representation of the device orientation.",
    },
    {
        "icon": "bi-cpu",
        "title": "ESP32 Processing",
        "text": "The ESP32 acts as the embedded controller between the sensor and the application layer.",
    },
    {
        "icon": "bi-diagram-3",
        "title": "Clear Data Flow",
        "text": "The complete path from sensor acquisition to software interaction is documented with a data flow diagram.",
    },
    {
        "icon": "bi-camera-video",
        "title": "Project Demonstration",
        "text": "A recorded video demonstrates the physical project and its operation.",
    },
    {
        "icon": "bi-code-slash",
        "title": "Modular Architecture",
        "text": "Routes, services, utilities and frontend assets are separated for easier development and testing.",
    },
]

TECHNOLOGIES = [
    ("Hardware", "ESP32", "Microcontroller for sensor acquisition and communication.", "bi-cpu"),
    ("Hardware", "MPU6050", "6-axis accelerometer and gyroscope module.", "bi-speedometer2"),
    ("Backend", "Python", "Application language for the Flask backend.", "bi-filetype-py"),
    ("Backend", "Flask", "Lightweight web framework exposing the application and API.", "bi-server"),
    ("Frontend", "HTML5 + CSS3", "Structure, layout and visual presentation.", "bi-code-slash"),
    ("Frontend", "Bootstrap", "Responsive layout and utility components.", "bi-bootstrap"),
    ("Frontend", "JavaScript", "Client-side interaction and live dashboard updates.", "bi-filetype-js"),
    ("Frontend", "AJAX / Fetch", "Retrieves JSON sensor data without full page refreshes.", "bi-arrow-repeat"),
    ("Visualization", "Three.js", "Browser-based 3D orientation visualization.", "bi-box"),
    ("Animation", "Animate.css", "Entrance and transition animations for the presentation UI.", "bi-stars"),
    ("Deployment", "Render", "Cloud deployment target for the Flask web application.", "bi-cloud-arrow-up"),
]

IMPLEMENTATION_STEPS = [
    ("01", "Sensing", "The MPU6050 captures accelerometer and gyroscope measurements."),
    ("02", "Acquisition", "The ESP32 reads the sensor through the I²C interface."),
    ("03", "Transmission", "The controller sends structured sensor information to the software layer."),
    ("04", "Processing", "The application layer validates and prepares values for visualization."),
    ("05", "Application Layer", "The Flask application organizes the project information and supporting web components."),
    ("06", "Presentation", "The website presents the system architecture, technologies and implementation clearly."),
    ("07", "Project Demonstration", "A recorded demonstration video shows the completed hardware project in operation."),
]

TEAM = [
    {
        "name": "Team Member 1",
        "role": "Embedded Systems",
        "contribution": "ESP32, MPU6050 wiring and sensor acquisition.",
        "icon": "bi-cpu",
    },
    {
        "name": "Team Member 2",
        "role": "Backend Development",
        "contribution": "Flask application, API and system integration.",
        "icon": "bi-server",
    },
    {
        "name": "Team Member 3",
        "role": "Frontend & Visualization",
        "contribution": "Dashboard UI, AJAX updates and 3D visualization.",
        "icon": "bi-display",
    },
    {
        "name": "Team Member 4",
        "role": "Documentation & Presentation",
        "contribution": "System documentation, diagrams and project presentation.",
        "icon": "bi-journal-text",
    },
]
