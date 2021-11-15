class Event_type:

    def __init__(self, description):
        self.description = description
        self.event_list = [] #Lista con instancias de la clase 'evento', con el mismo tipo que la instancia de esta clase

    def __repr__(self):
        return self.description

    def get_event_list(self):
         return self.event_list


    def add_ocurrence(self, ocurrence):
        #Agrega una ocurrencia del tipo de evento
        self.event_list.append(ocurrence)
