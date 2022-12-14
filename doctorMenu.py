# importing methods from doctor
from doctor import displayDoctorList
from doctor import searchDoctorById
from doctor import searchDoctorByName
from doctor import editDoctorInfo
from doctor import addDoctorToList


def doctorMenu():
    while True:
        print("Doctor's Menu\n", '0 - Return to main Menu\n',
              '1 - Display Doctors list\n', '2 - Search for doctor by ID', '3 - Search for doctor by name\n', '4 - add doctor\n', '5 - Edit doctor info')
        option = input('Enter option: ')
        if option == '0':
            break
        elif option == '1':
            print(displayDoctorList())
        elif option == '2':
            print(searchDoctorById())
        elif option == '3':
            print(searchDoctorByName())
        elif option == '4':
            print(addDoctorToList())
        elif option == '5':
            print(editDoctorInfo())
        else:
            print("Please enter a valid option(0-5)")



