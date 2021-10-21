from Citizen_record import citizen_record
from User import citizen, admin


class main_menu():

    def launch_main():
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Login\n\t2- Register\n\n(Type 'exit' if you want to close the program)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                __class__.enter_login_info()
            elif user_input == '2':
                __class__.register()
    
    def enter_login_info():
        user_input = ''
        while user_input != 'exit':
            user_Cuil = int(input('Enter Cuil: ')) 
            user_password = input('Enter password: ')
            for user in citizen_record.get_citizen_list():
                if user.get_cuil() == user_Cuil:
                    if user.get_password() == user_password:
                        __class__.login()
                        print('\nReturning to Main Menu...\n')
                        return ' '
            
            print("\n\tYour Cuil or password were incorrect. \n\tIf you want to try again, press enter.\n\tIf you want to leave to the Main Menu, type 'exit'\n")
            user_input = input("Press enter or type 'exit': ")
        
            
    
    def login():
        print("\nLogin succefull!\n")