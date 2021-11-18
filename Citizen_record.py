class CitizenRecord:
    def __init__(self):
        self.citizen_list = [] #Lista de ciudadanos registrados


    def register_citizen(self, new_citizen):
        #Debe agregar un ciudadano a la lista de ciudadanos registrados
        self.citizen_list.append(new_citizen)


    def unregister_citizen(self, citizen):
        self.citizen_list.remove(citizen)


    def get_citizen_list(self):
        return self.citizen_list




Citizen_record = CitizenRecord()
