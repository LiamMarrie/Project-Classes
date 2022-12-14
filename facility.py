class Facility():
    def __init__(self, name):
        self.name = name


def readFacilitiesFile():
    facilities_list = []
    with open('./txt/facilities.txt', mode='r') as file:  # Open the file in read
        for line in file:
            facility = line.strip()
            facilities_list.append(facility)
    for facility in facilities_list:
        print(facility)


def addFacility():
    # ask for user to enter new facility name
    new_facility = input("Enter Facility name: ")
    with open('./txt/facilities.txt', mode='a') as file:  # Open the file in append mode
        file.write(new_facility + '\n')  # Writes the new facility to the file
    return new_facility
