from time import sleep
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

i = 0

try:
    while True:
        i += 1
        message = f"Nachricht {i}"

        client.publish("test/topic", message)
        print(f"Gesendet: {message}")

        sleep(5)

except KeyboardInterrupt:
    print("Publisher beendet")

finally:
    client.disconnect()