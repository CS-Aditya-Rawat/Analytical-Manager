from kafka import KafkaConsumer
from prometheus_client import Counter

class Consumer:
    def __init__(self):
        self.group_id = "metrics-consumer-groupid"
        self.topic_name= "consumer-metrics";
        self.counter = Counter('kafka_events_received_total', 'Total number of kafka events received')
        self.enroll_now_clicked = Counter('enroll_now_clicked', 'Total number of users press Enroll Now Button')
        self.contact_us_clicked = Counter('contact_us_clicked', 'Total number of users clicked Contact us Button')
        self.consumer = KafkaConsumer(
            self.topic_name,
            group_id=self.group_id,
        )

    def listen(self):
        print(f"CURRENT COUNTER VALUE: {self.counter}")
        for message in self.consumer:
            event_data = message.value.decode('utf-8').strip()
            print(f"Received event: {message.value.decode('utf-8')}")
            if "userEnrollNowClicked" in event_data:
                self.enroll_now_clicked.inc()
            if "userClickedContact" in event_data:
                self.contact_us_clicked.inc()
            self.counter.inc()
