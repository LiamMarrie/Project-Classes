# importing methods from labClass
from labClass import displayLabsList
from labClass import addLabToList


def laboratoryMenu():
    while True:
        print("""Laboratory Menu
        0 - Return to main Menu
        1 - Display laboratories list
        2 - add laboratoy""")
        index = int(input('Option: '))
        if index == 0:
            break
        elif index == 1:
            print(displayLabsList())
        elif index == 2:
            print(addLabToList())
        else:
            print('Please enter a valid option (0-2)')
