from json import dumps
from kafka import KafkaProducer

class Producer:
    def __init__(self):
        self.topic_name= "consumer-metrics";
        self.bootstrap_server = "localhost:9092";
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_server, key_serializer=str.encode, value_serializer=str.encode)

    def send_user_event(self, event_data):
        try:
            if event_data == "userClickedContact":
                self.producer.send(self.topic_name, "userClickedContact", event_data)
            elif event_data == "userClickEnrollNow":
                self.producer.send(self.topic_name, "userEnrollNowClicked", event_data)
            self.producer.flush()
            print("Message produced successfully")
        except Exception as e:
            print(f"Error in Producing Data: {e}")

if __name__ == "__main__":
    producer = Producer()
    producer.send_user_event("userClick")
