class citizen_record:
    citizen_list = [] #Lista de ciudadanos registrados

    @classmethod
    def register_citizen(cls, new_citizen):
        #Debe agregar un ciudadano a la lista de ciudadanos registrados
        cls.citizen_list.append(new_citizen)

    @classmethod
    def get_citizen_list(cls):
        return cls.citizen_list
