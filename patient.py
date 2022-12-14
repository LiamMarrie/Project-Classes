class Patient:
    def __init__(self, id, name, diagnosis, gender, age):
        # Initialize instance variables for the patient's id, name, diagnosis, gender, and age
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    def formatPatientInfo(self):
        # Return the patient's information in a formatted string
        return "{}_{}_{}_{}_{}".format(self.id, self.name, self.diagnosis, self.gender, self.age)

    def __str__(self):
        patientsList = self.formatPatientInfo()
        return patientsList


def displayPatientsList():
    with open('./txt/patients.txt', mode='r') as f:
        displayPatientsList = []
        for line in f:
            displayPatientsList.append(line.replace('_', ' ').strip())
        return '\n'.join(displayPatientsList)


def searchPatientById():
    with open('./txt/patients.txt', mode='r') as f:
        patientID = input('Enter patient ID: ')
        lines = f.readlines()
        list = []
        for line in lines:
            if line.startswith(patientID):
                list.append(line.replace('_', ' '))
        if len(list) == 0:
            print('Patient with ID {} not in patient file'.format(patientID))
        else:
            return list[0]
    f.close()


def addPatientToList():
    with open("./txt/patients.txt", mode="a") as f:
        id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        diagnosis = input("Enter Patient Diagnosis: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")
        patient_str = f"{id} {name} {diagnosis} {gender} {age}"
        patient_str = patient_str.replace(" ", "_")
        f.write(patient_str)


def editPatientInfo():
    patient_id = input('Enter the patient ID: ')
    with open("./txt/patients.txt", mode="r") as f:
        lines = f.readlines()
        for patient, line in enumerate(lines):
            if line.startswith(patient_id):
                id, newName, newDiagnosis, newGender, newAge = line.split('_')
                newName = input('Enter the new name: ')
                newDiagnosis = input('Enter the new diagnosis: ')
                newGender = input('Enter the new gender: ')
                newAge = input('Enter the new age: ')
                lines[patient] = f"{id}_{newName}_{newDiagnosis}_{newGender}_{newAge}"
    with open("./txt/patients.txt", mode="w") as f:
        f.write('\n'.join(lines))
