from Event_type import Event_type

class Event:
    def __init__(self, type, coordinates):
        self.type = type #Debe ser una instancia de la clase 'event_type'
        self.coordinates = coordinates
        self.type.add_ocurrence(self) #Al inicializar el evento, se agrega a la lista de ocurrencias del tipo

    def get_coordinates(self):
        return self.coordinates

    def get_type(self):
        return self.type
