#Sistema para conceder y quitar privilegios de administrador a ciudadanos
from User import admin
from User import citizen
from Admin_record import Admin_record

class ABM:

    @classmethod
    def promote_citizen(cls, new_admin):
        #Esta funcion promueve al cuidadano a un rango mayor
        New_admin = admin(new_admin.cuil, new_admin.cellphone)
        Admin_record.admin_list.append(New_admin)
        #Falta poner que hay que sacarlod del citizen record

    @classmethod
    def demote_citizen(cls, admin):
        #Esta funcion degrada a un cuidadano a un rango menor
        for admins in Admin_record.admin_list:
            if admins == admin:
                Admin_record.admin_list.remove(admin)
                admin = citizen(admin.cuil, admin.cellphone)
                #Falta agregarlo a la citizen list


