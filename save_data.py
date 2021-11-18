import csv
from Citizen_record import Citizen_record
from Admin_record import Admin_record
from sensor_record import sensor_record
from Event_type_record import event_type_record

from User import Citizen, Admin, Sensor

class SaveData:

    def save(self):
        self.save_citizens()
        self.save_admins()
        self.save_sensors()

    def import_data(self):
        self.import_citizens()
        self.import_admins()
        self.import_sensors()

    def save_citizens(self):
        #Guarda registros de ciudadanos
        with open('registered_citizens.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            with open("registered_citizens.csv", "a") as a:
                writer = csv.writer(a)
                for citizen in Citizen_record.citizen_list:
                    for row in reader:
                        for col in row:
                            if col == str(citizen.cuil):
                                return
                    writer.writerow([citizen.cuil, citizen.cellphone, citizen.password, citizen.get_strikes()])

    def import_citizens(self):
        with open("registered_citizens.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) != 0:
                    citizen = Citizen(int(row[0]), int(row[1]), row[2])
                    citizen.strikes = int(row[3])
                    Citizen_record.register_citizen(citizen)


    def save_admins(self):
        with open("registered_admins.csv", "w") as r:
            writer = csv.writer(r)
            writer.writerow(['Cuil', 'cellphone', 'password'])
            for admin in Admin_record.get_admin_list():
                writer.writerow([admin.get_cuil(), admin.cellphone, admin.password])

    def import_admins(self):
        default_admin = Admin(0, 0, 'hola')
        with open("registered_admins.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) != 0:
                    for citizen in Citizen_record.get_citizen_list():
                        if citizen.cuil == int(row[0]):
                            default_admin.promote_citizen(citizen)


    def save_sensors(self):
        with open("registered_sensors.csv", "w") as r:
            writer = csv.writer(r)
            writer.writerow(['Type', 'coordinate x', 'coordinate y'])
            for sensor in sensor_record.get_sensors():
                writer.writerow([sensor.get_type(), sensor.get_coordinates()[0], sensor.get_coordinates()[1]])

    def import_sensors(self):
        with open("registered_sensors.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                for type in event_type_record.get_event_types():
                    if len(row) != 0:
                        if row[0] == type.description:
                            sensor = Sensor(type, (int(row[1]), int(row[2])))
                            sensor_record.add_sensor(sensor)

save_data = SaveData()
