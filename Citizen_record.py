from User import citizen
import csv
import unittest

class citizen_record:
    citizen_list = [] #Lista de ciudadanos registrados

    def register_citizen(user_Cuil, user_password, user_number):
        #Debe agregar un ciudadano a la lista de ciudadanos registrados
        new_citizen = citizen(user_Cuil, user_number) #Hay que agregar el password
        __class__.citizen_list.append(new_citizen)

    def validate_registration(Cuil, phone_number):
        #Debe ver si los datos ingresados concuerdan con datos en el Dataset de Anses
        with open ("Dataset.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                #La primer parte del if, compara con el cuil, la segunda parte del if, compara con el teléfono.
                if ("{0}".format(row[2])) == str(Cuil) and ("{0}".format(row[1])) == str(phone_number):
                    return True
                else:
                    return False

    def validate_login():
        #Debe ver si los datos ingresados concuerdan con algun ciudadano de citizen_list[]
        pass

    def get_citizen_list():
        return __class__.citizen_list

class test_user(unittest.TestCase):

    def test_dataset(self):
        citizen_record.register_citizen(9432, 'hola', 145)
        self.assertEqual(citizen_record.citizen_list[0].get_cuil(), 9432)

if __name__ == '__main__':
    unittest.main()