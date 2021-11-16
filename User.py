from abc import ABC, abstractmethod
from Event import Event
from Event_type import Event_type
from user_menu import citizen_menu, admin_menu
from Citizen_record import Citizen_record
from Admin_record import Admin_record
from Event_type_record import event_type_record
import csv
from monitoring import ranking_list

class User(ABC):
    def __init__(self, cuil, cellphone, password):
        self.cuil = cuil
        self.cellphone = cellphone
        self.password = password

    def report_event(self, type, coordinates):
        New_event = Event(type, coordinates)
        for events_type in event_type_record.get_event_types():
            if events_type == New_event.type:
                for event in events_type.get_event_list():
                    if event.coordinates == coordinates:
                        event.concurrence += 1
                        return True
                events_type.get_event_list().append(New_event)

    def get_cuil(self):
        return self.cuil

    def get_password(self):
        return self.password

    @abstractmethod
    def launch_user_menu(self):
        pass

    def __repr__(self):
        return f'{self.cuil}'

class Admin(User):

    @classmethod
    def get_event_type_list(self):
        return event_type_record.get_event_types()

    def ban(self, citizen):
        #Debe prohibir el acceso a su cuenta al ciudadano
        citizen.get_banned()

    def unban(self, citizen):
        #Debe rehabilitar el acceso a su cuenta al ciudadano
        citizen.get_unbanned()

    def promote_citizen(self, citizen):
        #Esta funcion promueve al cuidadano a un rango mayor
        Citizen_record.unregister_citizen(citizen)
        new_admin = Admin(citizen.cuil, citizen.cellphone, citizen.password)
        Admin_record.admin_list.append(new_admin)

    def demote_citizen(self, citizen):
        #Esta funcion degrada a un cuidadano a un rango menor
        for admins in Admin_record.admin_list:
            if admins == admin:
                Admin_record.admin_list.remove(admin)
                admin = citizen(admin.cuil, admin.cellphone)
                Citizen_record.register_citizen(admin)

    def create_event_type(self, descritpion):
        new_event_type = Event_type(descritpion)
        event_type_record.add_event_type(new_event_type)

    def create_sensor(self, type):
        #Debe crear una instancia de la clase 'sensor', con un tipo de evento asignado
        pass

    def launch_user_menu(self): #crea una instancia de la clase admin_menu y lo launchea
        new_admin_menu = admin_menu(self)
        new_admin_menu.action_menu()

class Citizen(User):
    def __init__(self, cuil, cellphone, password):
        super().__init__(cuil, cellphone, password)
        self.friend_list = []
        self.friend_request_list = []
        self.strikes = 0 #Cantidad de solicitudes rechazadas por otro ciudadanos

    def get_friend_requests(self):
        return self.friend_request_list

    def get_friend_list(self):
        return self.friend_list

    def get_strikes(self):
        return self.strikes

    def get_event_type_list(self):
        return Admin.get_event_type_list()

    def get_zone(self):
        with open("Dataset.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if int((row[2])) == self.cuil:
                        return row[3]

    def check_friend_requests(self):
        #Debe devolver(o mostrar por pantalla) la lista de de solicitudes de amistad
        print(self.friend_request_list)

    def send_friend_request(self, friend_request_reciever):
        #Debe enviarle una solicitud de amistad a otro ciudadano
        friend_request_reciever.update_request_list(self)

    def reject_friend_request(self, citizen):
        #Debe quitar de la lista de solicitudes al ciudadano y agregarle un strike
        for requester in self.friend_request_list:
            if requester == citizen:
                self.friend_request_list.remove(requester)
                requester.add_strike()

    def accept_friend_request(self, citizen):
        #Busca al ciudadano en la lista de solicitudes, lo remueve de esa lista y lo agrega a la lista de amigos
        for requester in self.friend_request_list:
            if requester == citizen:
                self.friend_request_list.remove(requester)
                self.friend_list.append(requester)

    def update_request_list(self, friend_request_sender):
        #Agrega al ciudadano que envia una solicitud a la lista de solicitudes
        self.friend_request_list.append(friend_request_sender)

    def add_strike(self):
        self.strikes += 1

    def get_banned(self):
        self.strikes = 5

    def get_unbanned(self):
        self.strikes = 0
        
    def report_citizen(self, other_citizen):
        # Adds strike al ciudadano reportado
        other_citizen.add_strike()

    def launch_user_menu(self): #crea una instancia de la clase citizen_menu y lo launchea
        new_citizen_menu = citizen_menu(self)
        if self.strikes >= 5:
            new_citizen_menu.banned_menu()
        else:
            new_citizen_menu.action_menu()

    def get_event_ranking(self):
        for ranking in ranking_list:
            if ranking.zone.description == self.get_zone():
                return ranking.get_ranking()

class Sensor:
    def __init__(self, event_type, coordinates):
        self.event_type = event_type
        self.coordinates = coordinates

    def report_event(self):
        #Debe crear una instancia de la clase 'evento', del tipo que tiene prestablecido el sensor
        pass

        

