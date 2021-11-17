from abc import ABC, abstractmethod
from utilities import user_searcher
from map import map

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
            try:
                user_input = int(input('\nEnter one of the above: '))
            except ValueError:
                print(f'\n\tYour input is not valid!\n\tPlease enter the number next to the event type you want to report\n')
                user_input = input(f"\nIf you want to cancel your report, enter 'exit'. If you want to try again, press enter: ")

            for type in event_type_list:
                if user_input == event_type_list.index(type):
                    new_event_type = type
                    try:
                        coord_x = int(input('\n\tEnter x coordinate of the event: '))
                        coord_y = int(input('\n\tEnter y coordinate of the event: '))
                    except ValueError:
                        print('\n\n\tThere was a problem with the coordinates you entered, make sure to enter integers when you try again')
                        return ''

                    self.user.report_event(new_event_type, (coord_x, coord_y))
                    print('\n\n\tEvent reported succesfully!')
                    return (new_event_type, (coord_x, coord_y))

    def event_map_menu(self):
        print('\n\tOpening map...\n')
        map.build_map()


class citizen_menu(user_menu):
    def action_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Manage Friends\n\t2- Report Event\n\t3- Events info\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.friend_menu()
            elif user_input == '2':
                self.report_menu()
            elif user_input == '3':
                self.monitoring_menu()

    def banned_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\tYou were banned from our platform due to breaking our policy rules\n\tYou can send a complaint to review your case at admin_mail@gmail.com\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input(f'Enter one of the above: ')

    def report_menu(self):
        event_info = super().report_menu()
        user_input = ''
        while user_input != 'exit':
            print(f"\n\tIs any of your friends participating in this event?")
            print(f'\n\t Friends: {self.user.get_friend_list()}')
            print(f"\n\n(Type 'exit' if you want to finish")
            user_input = (input(f'Enter their cuil: '))
            try:
                friend_cuil = int(user_input)
            except ValueError:
                pass
            if user_input != 'exit':
                friend = user_searcher.search_user(friend_cuil)
                friend.report_event(event_info[0], event_info[1])
    
    def friend_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Friend Requests\n\t2- Accept/Reject Friend\n\t3- Send Friend Request\n\t4- My Friends\n\n(Type 'exit' if you want to return)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.user.check_friend_requests()
            elif user_input == '2':
                try:
                    other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                except ValueError:
                    print('\n\nPlease enter a valid user Cuil!')
                    break
                other_user = user_searcher.search_user(other_user_cuil)
                self.accept_reject_menu(other_user)
            elif user_input == '3':
                try:
                    other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                except ValueError:
                    print('\n\nPlease enter a valid user Cuil!')
                    break
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
                return ''
            elif user_input == '2':
                self.user.reject_friend_request(other_user)
                return ''

    def monitoring_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Event map\n\t2- Top Events in my Zone\n\n(Type 'exit' if you want to return)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                self.event_map_menu()
            elif user_input == '2':
                self.ranking_menu()

    def ranking_menu(self):
        print()
        for event in self.user.get_event_ranking():
            print(f'Event: {event.type} Concurrence: {event.concurrence} Location: {event.coordinates}')

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
                try:
                    other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                except ValueError:
                    print('\n\nPlease enter a valid user Cuil!')
                    break
                other_user = user_searcher.search_user(other_user_cuil)
                self.ban_unban_menu(other_user)
            elif user_input == '2':
                try:
                    other_user_cuil = int(input(f"\n\n Enter other user's cuil: "))
                except ValueError:
                    print('\n\nPlease enter a valid user Cuil!')
                    break
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



class SensorMenu(user_menu):

    def action_menu(self):
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Report Event\n\n(Type 'exit' if you want to return to the login menu)")
            user_input = input('Enter one of the above: ')
            if user_input == '1':
                self.report_menu()

    def report_menu(self):
        self.user.report_event()
        print('\n\n\tEvent reported succesfully!')




