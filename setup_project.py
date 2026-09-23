"""Create the HoloGrip Flask project directory structure.

This script creates missing directories/files without overwriting application code.
It is safe to run again after the project has been developed further.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

DIRECTORIES = [
    "app",
    "app/routes",
    "app/services",
    "app/utils",
    "app/templates",
    "app/templates/errors",
    "app/static",
    "app/static/css",
    "app/static/js",
    "app/static/images",
    "app/static/images/team",
    "app/static/images/hardware",
    "app/static/images/diagrams",
    "app/static/models",
    "tests",
]

FILES = [
    "run.py",
    "config.py",
    "requirements.txt",
    "render.yaml",
    ".env.example",
    ".gitignore",
    "README.md",
    "app/__init__.py",
    "app/routes/__init__.py",
    "app/routes/main.py",
    "app/routes/api.py",
    "app/routes/health.py",
    "app/services/__init__.py",
    "app/services/sensor_service.py",
    "app/services/orientation.py",
    "app/services/keep_alive.py",
    "app/utils/__init__.py",
    "app/utils/constants.py",
    "app/utils/helpers.py",
    "app/utils/project_data.py",
    "app/templates/base.html",
    "app/templates/index.html",
    "app/templates/project.html",
    "app/templates/implementation.html",
    "app/templates/demo.html",
    "app/templates/team.html",
    "app/templates/errors/404.html",
    "app/templates/errors/500.html",
    "app/static/css/main.css",
    "app/static/css/home.css",
    "app/static/css/project.css",
    "app/static/css/implementation.css",
    "app/static/css/demo.css",
    "app/static/css/team.css",
    "app/static/js/main.js",
    "app/static/js/ajax.js",
    "app/static/js/sensor.js",
    "app/static/js/orientation.js",
    "app/static/js/animations.js",
    "tests/__init__.py",
    "tests/test_routes.py",
    "tests/test_api.py",
    "tests/test_orientation.py",
]


def main():
    for directory in DIRECTORIES:
        (ROOT / directory).mkdir(parents=True, exist_ok=True)

    created = 0
    for relative_path in FILES:
        path = ROOT / relative_path
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("", encoding="utf-8")
            created += 1

    print(f"Project root: {ROOT}")
    print(f"Directories ensured: {len(DIRECTORIES)}")
    print(f"Files checked: {len(FILES)}")
    print(f"New placeholder files created: {created}")


if __name__ == "__main__":
    main()
