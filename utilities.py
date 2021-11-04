from Citizen_record import citizen_record
from ABM import ABM
import csv
import unittest

class user_searcher:
    @staticmethod
    def search_user(user_cuil):
        for citizen in citizen_record.get_citizen_list():
            if citizen.get_cuil() == user_cuil:
                return citizen

        for admin in ABM.get_admin_list():
            if admin.get_cuil() == user_cuil:
                return admin

class user_validation:

    def validate_registration(Cuil, phone_number):
        #Debe ver si los datos ingresados concuerdan con datos en el Dataset de Anses
        with open("Dataset.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                #La primer parte del if, compara con el cuil, la segunda parte del if, compara con el teléfono.
                if ("{0}".format(row[2])) == str(Cuil) and ("{0}".format(row[1])) == str(phone_number):
                    return True
                else:
                    return False

    def validate_login(user_cuil, user_password):
        #Debe ver si los datos ingresados concuerdan con algun ciudadano de citizen_list[]
        user = user_searcher.search_user(user_cuil)
        try:
            password = user.get_password()
            if password == user_password:
                return True
            else:
                return False
        except AttributeError:
            return False

class test_user(unittest.TestCase):

    def test_validate_data_set(self):
        x = user_validation.validate_registration(9432, 145)
        self.assertEqual(x, True)

if __name__ == '__main__':
    unittest.main()
