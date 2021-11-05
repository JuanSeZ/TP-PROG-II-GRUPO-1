from User import citizen

class citizen_record:
    citizen_list = [] #Lista de ciudadanos registrados

    @classmethod
    def register_citizen(cls, user_Cuil, user_password, user_number):
        #Debe agregar un ciudadano a la lista de ciudadanos registrados
        new_citizen = citizen(user_Cuil, user_number, user_password)
        cls.citizen_list.append(new_citizen)

    @classmethod
    def get_citizen_list(cls):
        return cls.citizen_list
