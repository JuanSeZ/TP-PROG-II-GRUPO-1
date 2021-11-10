from abc import ABC, abstractmethod
from utilities import user_searcher

class user_menu(ABC):
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def action_menu(self): #Despliega la lista de acciones posibles y ejecuta metodos segun el input de usuario
        pass

class citizen_menu(user_menu):
    def action_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Manage Friends\n\t2- Report Event\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.friend_menu()
            elif user_input == '2':
                self.report_menu()
    
    def friend_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Friend Requests\n\t2- Accept/Reject Friend\n\t3- Send Friend Request\n\t4- My Friends\n\n(Type 'exit' if you want to return)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user.check_friend_requests()
            elif user_input == '2':
                other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                other_user = user_searcher.search_user(other_user_cuil)
                self.accept_reject_menu(other_user)
            elif user_input == '3':
                other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                self.user.send_friend_request(user_searcher.search_user(other_user_cuil))
            elif user_input == '4':
                print(self.user.get_friend_list())

    def accept_reject_menu(self, other_user):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Accept Friend\n\t2- Reject Friend\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user.accept_friend_request(other_user)
                return ''
            elif user_input == '2':
                self.user.reject_friend_request(other_user)
                return ''

class admin_menu(user_menu):
    def action_menu(self):
        pass
