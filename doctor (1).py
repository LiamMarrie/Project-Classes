class doctor:
    def __init__(self, id, name, specialty, schedule, qualifications, roomNbr):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.qualifications = qualifications
        self.roomNbr = roomNbr

    def formatDoctorInfo(self):
        return "{}_{}_{}_{}_{}".format(self.id, self.name, self.specialty, self.schedule, self.qualifications, self.roomNbr)

    def __str__(self):
        doctorList = self.formatDoctorInfo()
        return doctorList


def displayDoctorList():
    with open('./txt/doctors.txt', mode='r') as f:
        displayDoctorList = []
        for line in f:
            displayDoctorList.append(line.replace('_', ' ').strip())
        return '\n'.join(displayDoctorList)


def searchDoctorById():
    with open('./txt/doctors.txt', mode='r') as f:
        drID = input('Enter Dr. ID: ')
        lines = f.readlines()
        list = []
        for line in lines:
            if line.startswith(drID):
                list.append(line.replace('_', ' '))
        if len(list) == 0:
            print('Doctor With ID {} not in doctors file'.format(drID))
        else:
            return list[0]
    f.close()


def searchDoctorByName():
    with open("./txt/doctors.txt", "r") as file:
        drName = input("Enter Dr. Name: ")
        lines = file.readlines()
        list = []
        name = 0
        for line in lines:
            if drName in line:
                list.insert(name, line)
                name += 1
        if len(list) == 0:
            print("Patient with ID", drName, "not in patient file")
        else:
            print(list)


def addDoctorToList():
    with open("./txt/doctors.txt", mode="a") as f:
        id = input("Enter Dr. ID: ")
        name = input("Enter Dr. Name: ")
        specialty = input("Enter Dr. Specialty")
        schedule = input("Enter Dr. Schedule: ")
        qualifications = input("Enter Dr. Qualifications: ")
        roomNbr = input("Enter Dr. Room Number")
        doctor_str = f"{id} {name} {specialty} {schedule} {qualifications} {roomNbr}"
        doctor_str = doctor_str.replace(" ", "_")
        f.write(doctor_str)


def editDoctorInfo():
    drID = input('Enter Doctor ID: ')
    with open("./txt/doctors.txt", mode="r") as f:
        lines = f.readlines()
        for doctor, line in enumerate(lines):
            if line.startswith(drID):
                id, newName, newSpecialty, newSchedule, newQualifications, newRoomNbr = line.split(
                    '_')
                newName = input('Enter the new name: ')
                newSpecialty = input('Enter new Specialty: ')
                newSchedule = input('Enter new Schedule: ')
                newQualifications = input('Enter new Qualifications: ')
                newRoomNbr = input('Enter new Room Number: ')
                lines[doctor] = f"{id}_{newName}_{newSpecialty}_{newSchedule}_{newQualifications}_{newRoomNbr}"
    with open("./txt/doctors.txt", mode="w") as f:
        f.write('\n'.join(lines))
