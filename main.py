from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.producer import Producer
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from controller.consumer import Consumer
import threading

appConfig = Flask(__name__)
CORS(appConfig, resources={
    r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}
})

consumer = Consumer()
def start_kafka_consumer():
    consumer.listen()

# Start Kafka consumer thread
kafka_consumer_thread = threading.Thread(target=start_kafka_consumer)
kafka_consumer_thread.daemon = True
kafka_consumer_thread.start()

appConfig.wsgi_app = DispatcherMiddleware(appConfig.wsgi_app, {
    '/actuator/prometheus': make_wsgi_app()
})

@appConfig.route('/product/event', methods=['POST'])
def send_event_to_kafka():
    try:
        data = request.get_json()
        event = data.get('event')
        print(f"EVENT: {event}")
        producer = Producer()
        producer.send_user_event(event)
        return jsonify({'success': 'data'}), 200
    except Exception as e:
        print(f"Error handling event: {e}")
        return jsonify({'error': 'Failed to handle event'}), 500

if __name__ == "__main__":
    appConfig.run(port=8000)
