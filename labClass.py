class laboratory:
    def __init__(self, labName, cost):
        self.labName = labName
        self.cost = cost

    def formatLabInfo(self):
        return "{}_{}".format(self.labName, self.cost,)

    def __str__(self):
        labList = self.formatLabInfo()
        return labList


def displayLabsList():
    with open('./txt/laboratories.txt', mode='r') as f:
        displayLabsList = []
        for line in f:
            displayLabsList.append(line.replace('_', ' ').strip())
        return '\n'.join(displayLabsList)


def addLabToList():
    with open("./txt/laboratories.txt", mode="a") as f:
        laboratory = input("Enter Lab Name: ")
        cost = input("Enter Lab Cost: ")
        lab_str = f"{laboratory} {cost}"
        lab_str = lab_str.replace(" ", "_")
        f.write(lab_str)
