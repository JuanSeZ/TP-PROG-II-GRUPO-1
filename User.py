from abc import ABC, abstractmethod
import unittest

class user(ABC):
    def __init__(self, cuil, cellphone, password):
        self.cuil = cuil
        self.cellphone = cellphone
        self.password = password

    def report_event(self, type):
        #Debe crear una instancia de la clase 'evento', con un tipo especifico
        pass

    def get_cuil(self):
        return self.cuil

    def get_password(self):
        return self.password

    @abstractmethod
    def launch_user_menu(self):
        pass


class admin(user):
    def ban(self, citizen):
        #Debe prohibir el acceso a su cuenta al ciudadano
        citizen.get_banned()

    def unban(self, citizen):
        #Debe rehabilitar el acceso a su cuenta al ciudadano
        citizen.get_unbanned()

    def create_event_type(self, type):
        #Debe crear una instancia de la clase 'tipo_de_evento'
        pass

    def create_sensor(self, type):
        #Debe crear una instancia de la clase 'sensor', con un tipo de evento asignado
        pass

    def launch_user_menu(self): #crea una instancia de la clase admin_menu y lo launchea
        pass

class citizen(user):
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

    def check_friend_requests(self):
        #Debe devolver(o mostrar por pantalla) la lista de de solicitudes de amistad
        pass

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
        pass

class sensor:
    def __init__(self, event_type):
        self.event_type = event_type
    
    def report_event(self):
        #Debe crear una instancia de la clase 'evento', del tipo que tiene prestablecido el sensor
        pass

        
if __name__ == '__main__':
    unittest.main()
