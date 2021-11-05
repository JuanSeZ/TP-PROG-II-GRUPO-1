from Event_type import event_type

class event:
    def __init__(self, type, coordinates):
        self.type = type #Debe ser una instancia de la clase 'event_type'
        self.coordinates = coordinates
        #self.type.add_ocurrence(self) #Al inicializar el evento, se agrega a la lista de ocurrencias del tipo
