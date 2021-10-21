from User import user, citizen
import csv
import unittest

class citizen_record:
    citizen_list = [] #Lista de ciudadanos registrados

    
    
    #Usando la biblioteca csv, se pueden autenticar los datos presentes en el dataset de anses y compararlos con los datos ingresados por el ciudadano a la hora de registrarse.
    @staticmethod
    def register_citizen(citizen):
        #Debe agregar un ciudadano a la lista de ciudadanos registrados
        with open ("Dataset.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                #La primer parte del if, compara con el cuil, la segunda parte del if, compara con el teléfono.
                if ("{0}".format(row[2])) == str(citizen.cuil) and ("{0}".format(row[1])) == str(citizen.cellphone):
                    __class__.citizen_list.append(citizen)

    @staticmethod
    def get_citizen_list():
        return __class__.citizen_list

#Test que comprueba la validacion del usuario mediante el DATASET
class test_user(unittest.TestCase):

    def test_dataset(self):
        Juan = citizen(9432, 145)
        citizen_record.register_citizen(Juan)
        self.assertEqual(citizen_record.citizen_list, [Juan])

