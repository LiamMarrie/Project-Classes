# importing methods from facility 
from facility import readFacilitiesFile
from facility import addFacility


def facilityMenu():
    print('Facility Menu\n', '0 - Return to Main Menu\n',
          '1 - Display Facilities list\n', '2 - Add Facility')
    option = input('Enter option: ')

    while True:
        if option == '1':
            print(readFacilitiesFile())
        elif option == '2':
            print(addFacility())
        elif option == '0':
            break
        else:
            print('Please enter valid option(0-2).')


        # Prompt the user for the next option
        print('Facility Menu\n', '0 - Return to Main Menu\n',
              '1 - Display Facilities list\n', '2 - Add Facility')
        option=input('Enter option: ')

        # if option == '0':
        # print(mainMenu())

