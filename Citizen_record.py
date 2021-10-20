class citizen_record:
    citizen_list = [] #Lista de ciudadanos registrados

    def register_citizen(citizen):
        #Debe agregar un ciudadano a la lista de ciudadanos registrados
        __class__.citizen_list.append(citizen)
