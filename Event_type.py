class event_type:
    def __init__(self, description):
        self.description = description
        self.ocurrence_list = [] #Lista con instancias de la clase 'evento', con el mismo tipo que la instancia de esta clase

    def add_ocurrence(self, ocurrence):
        #Agrega una ocurrencia del tipo de evento
        self.ocurrence_list.append(ocurrence)