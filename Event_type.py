class Event_type:

    def __init__(self, description):
        self.description = description
        self.ocurrence_list = [] #Lista con instancias de la clase 'evento', con el mismo tipo que la instancia de esta clase

    def __repr__(self):
        return self.description

    def get_ocurrence_list(self):
         return self.ocurrence_list


    def add_ocurrence(self, ocurrence):
        #Agrega una ocurrencia del tipo de evento
        self.ocurrence_list.append(ocurrence)
