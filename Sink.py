#sub mit channel
#Daten einlesen, etwas ändern 
#in anderen channel chreiben
from Subscriber import Subscriber
from Publisher import Publisher

class Sink:
    
    def __init__(self):
        self.publisher = Publisher()
        self.subscriber = Subscriber("genData", prnt=self)

    def update(self, data):
        print(f"Empfangen: {data}")
        processed_data = data + " (verarbeitet)" # Beispiel für Datenverarbeitung
        print(f"Verarbeitet: {processed_data}")
        self.publisher.publish_message("processedData", processed_data)

if __name__ == "__main__":
    Sink()