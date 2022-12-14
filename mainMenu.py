# importing methods from all menu files
from patientMenu import patientMenu
from facilityMenu import facilityMenu
from doctorMenu import doctorMenu
from laboratory import laboratoryMenu
print('Welcome to the Alberta Rural Patient Care Management System\n')


def mainMenu():
    print('Main Menu\n', '0 - Close application\n ', '1 - Doctors\n',
          '2 - Facilities\n', '3 - Laboratories\n', '4 - Patients')
    option = input('Enter option: ')
    if option == '0':
        print('')
    elif option == '1':
        print(doctorMenu())
    elif option == '2':
        print(facilityMenu())
    elif option == '3':
        print(laboratoryMenu())
    elif option == '4':
        print(patientMenu())
    return mainMenu()


mainMenu()
