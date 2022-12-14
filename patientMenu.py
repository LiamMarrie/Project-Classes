# importing methods from patient.py
from patient import displayPatientsList
from patient import searchPatientById
from patient import editPatientInfo
from patient import addPatientToList


def patientMenu():
    while True:
        print('Patient Menu \n', '0 - Return to Main Menu \n', "1 - Display patient's list \n",
              '2 - Search for patient by ID \n', '3 - Add patient \n', '4 - Edit patient info')
        index = int(input('Option: '))
        if index == 0:
            break
        elif index == 1:
            print(displayPatientsList())  # works
        elif index == 2:
            print(searchPatientById())  # works
        elif index == 3:
            print(addPatientToList())  # works
        elif index == 4:
            print(editPatientInfo())
        else:
            print('Please enter a valid option (0-4)')
