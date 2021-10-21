#Sistema para conceder y quitar privilegios de administrador a ciudadanos
from User import admin
from User import citizen
class ABM:

    def __init__(self):
        self.admin_list = []


    def promote_citizen(self, new_admin):
        #Esta funcion promueve al cuidadano a un rango mayor
        New_admin = admin(new_admin.cuil, new_admin.cellphone)
        self.admin_list.append(New_admin)
        #Falta poner que hay que sacarlod del citizen record

    def demote_citizen(self, admin):
        #Esta funcion degrada a un cuidadano a un rango menor
        for admins in self.admin_list:
            if admins == admin:
                self.admin_list.remove(admin)
                admin = citizen(admin.cuil, admin.cellphone)
