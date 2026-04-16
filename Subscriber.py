import paho.mqtt.client as mqtt
import sys

class Subscriber:
    topic = ""
    def __init__(self, topic = "genData", broker_address = "localhost", broker_port = 1883, prnt = None):
        self.topic = topic
        self.prnt = prnt

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker_address, broker_port, 60)
        # Wartet dauerhaft auf Nachrichten
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Verbunden mit Ergebniscode:", rc)
        client.subscribe(self.topic)
        print(f"Abonniert: {self.topic}")

    def on_message(self, client, userdata, msg):
        print(f"Nachricht empfangen:")
        print(f"  Topic: {msg.topic}")
        print(f"  Payload: {msg.payload.decode()}")
        if self.prnt is not None:#cursed
            self.prnt.update(msg.payload.decode())

    

    

def main():
    print(sys.argv)
    Subscriber(sys.argv[1] if len(sys.argv) > 1 else "genData")


if __name__ == "__main__":
    main()