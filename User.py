from abc import ABC

class user(ABC):
    def __init__(self, cuil, cellphone, password):
        self.cuil = cuil
        self.cellphone = cellphone
        self.password = password

    def report_event(self, type):
        #Debe crear una instancia de la clase 'evento', con un tipo especifico
        pass

class admin(user):
    def ban(self, citizen):
        #Debe prohibir el acceso a su cuenta al ciudadano
        pass

    def unban(self, citizen):
        #Debe rehabilitar el acceso a su cuenta al ciudadano
        pass

    def create_event_type(self, type):
        #Debe crear una instancia de la clase 'tipo_de_evento'
        pass

    def create_sensor(self, type):
        #Debe crear una instancia de la clase 'sensor', con un tipo de evento asignado
        pass

class citizen(user):
    def __init__(self, cuil, cellphone):
        super.__init__(cuil, cellphone)
        friend_list = []
        friend_request_list = []
        strikes = 0 #Cantidad de solicitudes rechazadas por otro ciudadanos

    def check_friend_requests(self):
        #Debe devolver(o mostrar por pantalla) la lista de de solicitudes de amistad
        pass

    def send_friend_request(self, citizen):
        #Debe enviarle una solicitud de amistad a otro ciudadano
        pass

    def reject_friend_request(self, citizen):
        #Debe quitar de la lista de solicitudes al ciudadano y agregarle un strike
        pass

class sensor:
    def __init__(self, event_type):
        self.event_type = event_type
    
    def report_event(self):
        #Debe crear una instancia de la clase 'evento', del tipo que tiene prestablecido el sensor
        pass
