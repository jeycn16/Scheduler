import random

class person:
    def __init__(self, name, skill, stationAssigned, reviewed):
        self.name = name
        self.skill = skill
        self.stationAssigned = stationAssigned
        self.reviewed = reviewed

def chooseSomeoneToFillaStation(station, operatorList):
    OperatorsAbleToPerform = []
    cntr = 0

    for index, operator in enumerate(operatorList):
        operator.reviewed = 0
        if operator.skill[station] == 1:
            OperatorsAbleToPerform.append(index)
    # print("for station ", station, " operators ", OperatorsAbleToPerform, " can perform this activity")

    while True:
        randomIndex = random.choice(OperatorsAbleToPerform)     #randrange(0, len(operatorList),1)
        if operatorList[randomIndex].stationAssigned == -1:
            if operatorList[randomIndex].reviewed == 0:
                print(operatorList[randomIndex].name)
                operatorList[randomIndex].stationAssigned = randomIndex
                break
            else:
                operatorList[randomIndex].reviewed = 1
                cntr += 1
                if cntr == len(OperatorsAbleToPerform):
                    print("All options have been evaluated")
                    break
        else:
            if operatorList[station].stationAssigned == randomIndex:
                print(operatorList[station].name + " already assigned to station " + str(station))
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    operator_0 = person("Amy", [1, 0, 1, 1, 0], 2, 0)
    operator_1 = person("Maria", [0, 1, 0, 0, 1], -1, 0)
    operator_2 = person("Julia", [0, 1, 1, 0, 0], -1, 0)
    operator_3 = person("Pepe", [1, 0, 0, 1, 0], 0, 0)
    operator_4 = person("Minerva", [0, 1, 1, 0, 1], 1, 0)

    operatorList = [operator_0, operator_1, operator_2, operator_3, operator_4]
    for x in range(5):
        chooseSomeoneToFillaStation(x, operatorList)
