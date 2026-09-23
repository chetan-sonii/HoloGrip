from pathlib import Path

ROOT = Path(__file__).resolve().parent

DIRECTORIES = [
    'app',
    'app/routes',
    'app/services',
    'app/utils',
    'app/templates',
    'app/templates/errors',
    'app/static/css',
    'app/static/js',
    'app/static/images/team',
    'app/static/images/hardware',
    'app/static/images/diagrams',
    'app/static/models',
    'tests',
]


def create_structure():
    for directory in DIRECTORIES:
        (ROOT / directory).mkdir(parents=True, exist_ok=True)

    print(f'Project structure created at: {ROOT}')
    print(f'Created {len(DIRECTORIES)} directories.')


if __name__ == '__main__':
    create_structure()