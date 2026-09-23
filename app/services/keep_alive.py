import os
import threading
import time

import requests

_started = False


def start_keep_alive(app):
    """Optionally ping the public Render URL every N seconds."""
    global _started

    if _started:
        return

    app_url = app.config.get('APP_URL') or os.getenv('APP_URL', '').rstrip('/')
    interval = int(app.config.get('SELF_PING_INTERVAL', 10))

    if not app_url:
        return

    if app.debug and os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        return

    def worker():
        while True:
            time.sleep(interval)
            try:
                requests.get(f'{app_url}/health', timeout=5)
            except requests.RequestException:
                pass

    threading.Thread(target=worker, name='render-self-ping', daemon=True).start()
    _started = True
