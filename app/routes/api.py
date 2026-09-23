from flask import Blueprint, jsonify

from app.services.sensor_service import get_sensor_snapshot

api_bp = Blueprint('api', __name__)


@api_bp.get('/sensor')
def sensor():
    return jsonify(get_sensor_snapshot())


@api_bp.get('/status')
def status():
    snapshot = get_sensor_snapshot()
    return jsonify({
        'connected': snapshot['connected'],
        'source': snapshot['source'],
        'timestamp': snapshot['timestamp'],
    })
