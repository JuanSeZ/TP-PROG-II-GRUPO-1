from abc import ABC, abstractmethod
from utilities import user_searcher

class user_menu(ABC):
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def action_menu(self): #Despliega la lista de acciones posibles y ejecuta metodos segun el input de usuario
        pass

    def report_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f'-----------------------------------\n\n\tSelect an event type to report:\n')
            event_type_list = self.user.get_event_type_list()
            for type in event_type_list:
                print(f'\t\t{event_type_list.index(type)} - {type}')
            user_input = int(input('\nEnter one of the above: '))
            for type in event_type_list:
                if user_input == event_type_list.index(type):
                    new_event_type = type
                    coord_x = int(input('\n\tEnter x coordinate of the event: '))
                    coord_y = int(input('\n\tEnter y coordinate of the event: '))
                    self.user.report_event(new_event_type, (coord_x, coord_y))
                    print('\n\n\tEvent reported succesfully!')
                    return ''

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

    def banned_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\tYou were banned from our platform due to breaking our policy rules\n\tYou can send a complaint to review your case at admin_mail@gmail.com\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')

    
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
                print(f'\n\n\tRequest sent successfully!')
            elif user_input == '4':
                print(self.user.get_friend_list())

    def accept_reject_menu(self, other_user):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Accept Friend\n\t2- Reject Friend\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user.accept_friend_request(other_user)
            elif user_input == '2':
                self.user.reject_friend_request(other_user)

class admin_menu(user_menu):
    def action_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Manage Users\n\t2- Report Event\n\t3- Create Event Type\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user_manager_menu()
            elif user_input == '2':
                self.report_menu()
            elif user_input == '3':
                self.event_type_menu()

    def user_manager_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Ban/Unban Citizen\n\t2- Promote/Demote Admin\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                other_user = user_searcher.search_user(other_user_cuil)
                self.ban_unban_menu(other_user)
            elif user_input == '2':
                other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                other_user = user_searcher.search_user(other_user_cuil)
                self.promote_demote_menu(other_user)

    def ban_unban_menu(self, other_user):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Ban Citizen\n\t2- Unban Citizen\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user.ban(other_user)
                return ''
            elif user_input == '2':
                self.user.unban(other_user)
                return ''

    def promote_demote_menu(self, other_user):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Promote User\n\t2- Demote User\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user.promote_citizen(other_user)
                return ''
            elif user_input == '2':
                self.user.demote_citizen(other_user)
                return ''

    def event_type_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Check Current Types\n\t2- Create New Event Type \n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                print(f'\n\n{self.user.get_event_type_list()}')
            elif user_input == '2':
                type_description = input(f'\n\nEnter a description of the new event type: ')
                self.user.create_event_type(type_description)
