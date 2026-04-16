from time import sleep
import paho.mqtt.client as mqtt




class Publisher:
    def __init__(self, broker_address = "localhost", broker_port = 1883):
    
        self.client = mqtt.Client()
        self.client.connect(broker_address, broker_port, 60)

    
    def publish_message(self, topic = "test/topic", message = "default message"):
        self.client.publish(topic, message)
        print(f"Gesendet: {message} auf {topic}")

