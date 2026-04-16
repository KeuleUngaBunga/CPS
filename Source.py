#random generierte Daten in Channel schreiben
from Publisher import Publisher
import time


class Source:
    def __init__(self):
        self.publisher = Publisher()
        self.generate_data()

    def generate_data(self):
        i = 0
        while True:
            i += 1
            data = f"Data {i}"
            print(f"Generated: {data}")
            self.publisher.publish_message("genData", data)
            time.sleep(5) # Warte 5 Sekunden, bevor die nächste Nachricht generiert wird
            # Hier könnte man die


if __name__ == "__main__":
    Source()