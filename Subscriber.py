import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Verbunden mit Ergebniscode:", rc)
    client.subscribe("test/topic")
    print("Abonniert: test/topic")

def on_message(client, userdata, msg):
    print(f"Nachricht empfangen:")
    print(f"  Topic: {msg.topic}")
    print(f"  Payload: {msg.payload.decode()}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Wartet dauerhaft auf Nachrichten
client.loop_forever()