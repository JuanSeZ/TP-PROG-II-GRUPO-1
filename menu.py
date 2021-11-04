from Citizen_record import citizen_record
from utilities import user_searcher, user_validation

class main_menu():

    def launch_main():
        user_input = ''
        while user_input != 'exit':
            print(f"-----------------------------------\n\n\t1- Login\n\t2- Register\n\n(Type 'exit' if you want to close the program)")
            user_input = input(f'Enter one of the above: ')
            if user_input == '1':
                __class__.enter_login_info()
            elif user_input == '2':
                __class__.enter_register_info()

    def enter_login_info():
        user_input = ''
        while user_input != 'exit':
            user_Cuil = int(input('Enter Cuil: ')) 
            user_password = input('Enter password: ')
            if user_validation.validate_login(user_Cuil, user_password): #Hay que implementar el metodo validate_login()
                __class__.login(user_searcher.search_user(user_Cuil))
                print('\nReturning to Main Menu...\n')
                return ' '
            
            print("\n\tYour Cuil or password were incorrect. \n\tIf you want to try again, press enter.\n\tIf you want to leave to the Main Menu, type 'exit'\n")
            user_input = input("Press enter or type 'exit': ")
        
    def enter_register_info():
        user_input = ''
        while user_input != 'exit':
            user_Cuil = int(input('Enter Cuil: '))
            user_number = int(input('Enter phone number: '))
            user_password = input('Enter password: ')
            user_password_validation = input('Enter password again: ')

            if user_validation.validate_registration(user_Cuil, user_number) and user_password == user_password_validation: #Hay que implementar el metodo validate_registration()
                __class__.register(user_Cuil, user_password, user_number)
                print('\nReturning to Main Menu...\n')
                return ' '
            
            print("\n\tSomething went wrong.\n\tBe sure to put your Cuil, phone number and passwords(both times) correctly \n\tIf you want to try again, press enter.\n\tIf you want to leave to the Main Menu, type 'exit'\n")
            user_input = input("Press enter or type 'exit': ")
    
    def login(user):
        print("\nLogin was succefull!\n")
        user.action_menu()

    def register(user_Cuil, user_password, user_number):
        print("\nRegistration was succefull!")
        citizen_record.register_citizen(user_Cuil, user_password, user_number)


main_menu.launch_main()
