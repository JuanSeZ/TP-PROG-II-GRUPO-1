import csv

from Citizen_record import Citizen_record
from User import Citizen, Sensor
from utilities import user_searcher, user_validation
from ABM import ABM
from Event_type_record import event_type_record
from Event_type import Event_type
from sensor_record import sensor_record
from monitoring import general_ranking
from save_data import Save_data

class MainMenu:

    def launch_main(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Log in\n\t2- Register\n\n(Type 'exit' if you want to close the program)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.sensor_or_user_menu()
            elif user_input == '2':
                self.enter_register_info()
        Save_data.save()

    def sensor_or_user_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Log in as User\n\t2- Log in as Sensor\n\n(Type 'exit' if you want to go back)")
            user_input = input('Enter one of the above: ')
            if user_input == '1':
                self.enter_login_info()
            elif user_input == '2':
                self.sensor_login()

    def sensor_login(self):
        user_input = ''
        sensors = sensor_record.get_sensors()
        for sensor in sensors:
            print(f'\n\t{sensors.index(sensor)} - Type: {sensor.get_type()} Coordinates: {sensor.get_coordinates()}')
        print('')
        user_input = int(input('Choose one of the above: '))
        for sensor in sensors:
            if user_input == sensors.index(sensor):
                sensor.launch_user_menu()



    def enter_login_info(self):
        user_input = ''
        while user_input != 'exit':
            try:
                user_Cuil = int(input('Enter Cuil: '))
            except ValueError:
                user_Cuil = -1
            user_password = input('Enter password: ')
            if user_validation.validate_login(user_Cuil, user_password):
                self.login(user_searcher.search_user(user_Cuil))
                print('\nReturning to Main Menu...\n')
                return ' '
            
            print("\n\tYour Cuil or password were incorrect. \n\tIf you want to try again, press enter.\n\tIf you want to leave to the Main Menu, type 'exit'\n")
            user_input = input("Press enter or type 'exit': ")


    def enter_register_info(self):
        user_input = ''
        while user_input != 'exit':
            try:
                user_Cuil = int(input('Enter Cuil: '))
                user_number = int(input('Enter phone number: '))
            except ValueError:
                user_Cuil = -1
                user_number = -1
            user_password = input('Enter password: ')
            user_password_validation = input('Enter password again: ')

            if user_validation.validate_registration(user_Cuil, user_number) and user_password == user_password_validation: #Hay que implementar el metodo validate_registration()
                self.register(user_Cuil, user_password, user_number)
                print('\nReturning to Main Menu...\n')
                return ' '
            
            print("\n\tSomething went wrong.\n\tBe sure to put your Cuil, phone number and passwords(both times) correctly \n\tIf you want to try again, press enter.\n\tIf you want to leave to the Main Menu, type 'exit'\n")
            user_input = input("Press enter or type 'exit': ")
    
    def login(self, user):
        print("\nLogin was succefull!\n")
        user.launch_user_menu()

    def register(self, user_Cuil, user_password, user_number):
        print("\nRegistration was succefull!")
        new_citizen = Citizen(user_Cuil, user_number, user_password)
        Citizen_record.register_citizen(new_citizen)




#Prueba Menu

#fake_citizen = Citizen(9432, 145, 'hola')
#Citizen_record.register_citizen(fake_citizen)
#fake_friend = Citizen(12, 390, 'chau')
#Citizen_record.register_citizen(fake_friend)
#fake_friend.send_friend_request(fake_citizen)

#robo = Event_type('Robo')
#recital = Event_type('Recital')
#event_type_record.add_event_type(robo)
#event_type_record.add_event_type(recital)
#new_sensor = Sensor(robo, (1, 1))
#sensor_record.add_sensor(new_sensor)
#Se crea un admin por default
default_admin = Citizen(0, 0, 'admin')
Citizen_record.register_citizen(default_admin)
ABM.promote_citizen(default_admin)

#Se instancia e inicia el menu
general_ranking.import_ranking()
Main_menu = MainMenu()
Main_menu.launch_main()
general_ranking.record_ranking()

