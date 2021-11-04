from abc import ABC, abstractmethod

class user_menu(ABC):
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def action_menu(self): #Despliega la lista de acciones posibles y ejecuta metodos segun el input de usuario
        pass

class citizen_menu(user_menu):
    def action_menu(self):
        pass

class admin_menu(user_menu):
    def action_menu(self):
        pass
