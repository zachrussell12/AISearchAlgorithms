
class HarryPotter:
    
    def __init__(self):
        self.moveCost = 1
        self.dstryHXCost = 3

    def move(self):
        return self.moveCost
    
    def dstryHX(self):
        return self.dstryHXCost
    
class AlbusDumbledore:

    def __init__(self):
        self.moveCost = 2
        self.dstryHXCost = 1

    def move(self):
        return self.moveCost
    
    def dstryHX(self):
        return self.dstryHXCost
    
class Locations:

    def __init__(self):
        self.hw = {"connections": ["hm"], "horcrux1": False, "horcrux2": False}
        self.hm = {"connections": ["gs", "hw", "ln"], "horcrux1": True, "horcrux2": False}
        self.gs = {"connections": ["hm", "ln"], "horcrux1": False, "horcrux2": True}
        self.ln = {"connections": ["gs", "hm"], "horcrux1": False, "horcrux2": False}

    def getConnections(self, location):
        return getattr(self, location)["connections"]
    
    def checkHX1(self, location):
        return getattr(self, location)["horcrux1"]
    
    def checkHX2(self, location):
        return getattr(self, location)["horcrux2"]
    

def DFS_Search():


    locater = Locations()
    HP = HarryPotter()
    AD = AlbusDumbledore()
    j = 0
    initialState = ["ln", "hw", False, False]
    expandedNodesStack = []
    visitedStates = []
    checkGoalState = initialState.copy()
    totalcost = 0

    while checkGoalState[2] == False or checkGoalState[3] == False:
    #while j != 2:

        currentState = []

        travelPaths = {"HP": [], "AD": []}

        if j == 0:
            currentState = initialState.copy()
        else:
            currentState = expandedNodesStack.pop()

        #print("*" * 30)
        #print("Current State: ", currentState)

        visitedStates.append(currentState)

        for i in range(2):
            if i == 0:
                travelPaths["HP"] = (locater.getConnections(currentState[i]))
            else:
                travelPaths["AD"] = (locater.getConnections(currentState[i]))

        #print(travelPaths)

        for i in range(len(travelPaths["HP"])):
            if [travelPaths["HP"][i], currentState[1], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3]])

        for i in range(len(travelPaths["AD"])):
            if [currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]])

        if locater.checkHX1(currentState[0]) or locater.checkHX1(currentState[1]):
            if [currentState[0], currentState[1], True, currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3]])

        if locater.checkHX2(currentState[0]) or locater.checkHX2(currentState[1]):
            if [currentState[0], currentState[1], currentState[2], True] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True])


        #print("Possible States: ",  expandedNodesStack)
        #print("*" * 30)

        checkGoalState.clear()
        checkGoalState = currentState.copy()

        j = j + 1

    print("Goal State Reached: ", checkGoalState)

    for i in range(len(visitedStates)):
        if i == len(visitedStates)-1:
            pass
        elif visitedStates[i][0] != visitedStates[i+1][0]:
            totalcost += HP.move()
        elif visitedStates[i][1] != visitedStates[i+1][1]:
            totalcost += AD.move()
        elif visitedStates[i][2] != visitedStates[i+1][2]:
            if visitedStates[i+1][0] == "hm":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
        else:
            if visitedStates[i+1][0] == "gs":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
            
    print("Pathing: ", visitedStates)
    print("Total Cost: ", totalcost)

def BFS_Search():


    locater = Locations()
    HP = HarryPotter()
    AD = AlbusDumbledore()
    j = 0
    initialState = ["ln", "hw", False, False]
    expandedNodesStack = []
    visitedStates = []
    checkGoalState = initialState.copy()
    totalcost = 0

    while checkGoalState[2] == False or checkGoalState[3] == False:
    #while j != 2:

        currentState = []

        travelPaths = {"HP": [], "AD": []}

        if j == 0:
            currentState = initialState.copy()
        else:
            currentState = expandedNodesStack.pop(0)

        #print("*" * 30)
        #print("Current State: ", currentState)

        visitedStates.append(currentState)

        for i in range(2):
            if i == 0:
                travelPaths["HP"] = (locater.getConnections(currentState[i]))
            else:
                travelPaths["AD"] = (locater.getConnections(currentState[i]))

        #print(travelPaths)

        for i in range(len(travelPaths["HP"])):
            if [travelPaths["HP"][i], currentState[1], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3]])

        for i in range(len(travelPaths["AD"])):
            if [currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]])

        if locater.checkHX1(currentState[0]) or locater.checkHX1(currentState[1]):
            if [currentState[0], currentState[1], True, currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3]])

        if locater.checkHX2(currentState[0]) or locater.checkHX2(currentState[1]):
            if [currentState[0], currentState[1], currentState[2], True] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True])


        #print("Possible States: ",  expandedNodesStack)
        #print("*" * 30)

        checkGoalState.clear()
        checkGoalState = currentState.copy()

        j = j + 1

    print("Goal State Reached: ", checkGoalState)

    for i in range(len(visitedStates)):
        if i == len(visitedStates)-1:
            pass
        elif visitedStates[i][0] != visitedStates[i+1][0]:
            totalcost += HP.move()
        elif visitedStates[i][1] != visitedStates[i+1][1]:
            totalcost += AD.move()
        elif visitedStates[i][2] != visitedStates[i+1][2]:
            if visitedStates[i+1][0] == "hm":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
        else:
            if visitedStates[i+1][0] == "gs":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
            
    print("Pathing: ", visitedStates)
    paths = [[visitedStates[0]]]
    j = 0

    for i in range(len(visitedStates)):
        if i == len(visitedStates)-1:
            pass
        else:
            differingIndex = [i for i, item in enumerate(visitedStates[i]) if item not in visitedStates[i+1]]
            if differingIndex == 0:
                if locater.getConnections(visitedStates[i][0]) in visitedStates[i+1][0]:
                    paths[j].append(visitedStates[i+1])
                    j = j + 1
            elif  differingIndex == 1:
                if locater.getConnections(visitedStates[i][1]) in visitedStates[i+1][1]:
                    paths[j].append(visitedStates[i+1])
                    j = j + 1

    
    #print("Total Cost: ", totalcost)

    
#print("*" * 200)
#print()
#print("DFS SEARCH: ")
#DFS_Search()
#print()
#print("*" * 200)

print()
print("BFS SEARCH: ")
BFS_Search()
print()
print("*" * 200)

