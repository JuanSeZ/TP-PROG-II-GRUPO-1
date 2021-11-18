class AdminRecord:

    def __init__(self):
        self.admin_list = []


    def get_admin_list(self):
        return self.admin_list

    def add_default_admin(self, default_admin):
        self.admin_list.append(default_admin)

    def remove_default_admin(self, default_admin):
        self.admin_list.remove(default_admin)

Admin_record = AdminRecord()
