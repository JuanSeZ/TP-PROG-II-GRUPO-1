#Sistema para conceder y quitar privilegios de administrador a ciudadanos
from User import admin
from User import citizen
from Admin_record import Admin_record
from Citizen_record import citizen_record

class ABM:

    @classmethod
    def promote_citizen(cls, old_citizen):
        #Esta funcion promueve al cuidadano a un rango mayor
        citizen_record.unregister_citizen(old_citizen)
        new_admin = admin(old_citizen.cuil, old_citizen.cellphone, old_citizen.password)
        Admin_record.admin_list.append(new_admin)

    @classmethod
    def demote_citizen(cls, admin):
        #Esta funcion degrada a un cuidadano a un rango menor
        for admins in Admin_record.admin_list:
            if admins == admin:
                Admin_record.admin_list.remove(admin)
                admin = citizen(admin.cuil, admin.cellphone)
                citizen_record.register_citizen(admin)
