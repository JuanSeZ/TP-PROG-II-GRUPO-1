#Sistema para conceder y quitar privilegios de administrador a ciudadanos
from User import Admin
from User import Citizen
from Admin_record import Admin_record
from Citizen_record import Citizen_record

class ABM:

    @classmethod
    def promote_citizen(cls, old_citizen):
        #Esta funcion promueve al cuidadano a un rango mayor
        Citizen_record.unregister_citizen(old_citizen)
        new_admin = Admin(old_citizen.cuil, old_citizen.cellphone, old_citizen.password)
        Admin_record.admin_list.append(new_admin)

    @classmethod
    def demote_citizen(cls, admin):
        #Esta funcion degrada a un cuidadano a un rango menor
        for admins in Admin_record.admin_list:
            if admins == admin:
                Admin_record.admin_list.remove(admin)
                admin = Citizen(admin.cuil, admin.cellphone)
                Citizen_record.register_citizen(admin)
