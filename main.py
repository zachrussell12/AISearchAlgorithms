
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
            
    print("Pathing: ")
    for state in visitedStates:
        if state == visitedStates[len(visitedStates)-1]:
            print(f"{state}")
        else:
            print(f"{state} -> ", end="")
    print("Total Cost: ", totalcost)

def BFS_Search():

    locater = Locations()
    HP = HarryPotter()
    AD = AlbusDumbledore()
    j = 0
    initialState = ["ln", "hw", False, False]
    expandedNodesStack = []
    visitedStates = []
    treeRepresentation = {f"{initialState}": []}
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
            treeRepresentation[f"{currentState}"] = []

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
                treeRepresentation[f"{currentState}"].append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3]])

        for i in range(len(travelPaths["AD"])):
            if [currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]])
                treeRepresentation[f"{currentState}"].append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]])

        if locater.checkHX1(currentState[0]) or locater.checkHX1(currentState[1]):
            if [currentState[0], currentState[1], True, currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3]])
                treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], True, currentState[3]])

        if locater.checkHX2(currentState[0]) or locater.checkHX2(currentState[1]):
            if [currentState[0], currentState[1], currentState[2], True] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True])
                treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], currentState[2], True])


        #print("Possible States: ",  expandedNodesStack)
        #print("*" * 30)

        checkGoalState.clear()
        checkGoalState = currentState.copy()

        j = j + 1

    print("Goal State Reached: ", checkGoalState)
            
    searchState = checkGoalState
    pathing = []
    
    while searchState != initialState:
        for i in range(len(visitedStates)):
            for j in range(len(treeRepresentation[f"{visitedStates[i]}"])):
                if treeRepresentation[f"{visitedStates[i]}"][j] == searchState:
                    pathing.insert(0, searchState)
                    searchState = visitedStates[i]

    pathing.insert(0, initialState)
    
    print("Pathing: ")
    for state in pathing:
        if state == pathing[len(pathing)-1]:
            print(f"{state}")
        else:
            print(f"{state} -> ", end="")

    for i in range(len(pathing)):
        if i == len(pathing)-1:
            pass
        elif pathing[i][0] != pathing[i+1][0]:
            totalcost += HP.move()
        elif pathing[i][1] != pathing[i+1][1]:
            totalcost += AD.move()
        elif pathing[i][2] != pathing[i+1][2]:
            if pathing[i+1][0] == "hm":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
        else:
            if pathing[i+1][0] == "gs":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()

    print("Total Cost: ", totalcost)

def ID_Search(providedDepth= 0):

    locater = Locations()
    HP = HarryPotter()
    AD = AlbusDumbledore()
    j = 0
    depth = providedDepth
    initialState = ["ln", "hw", False, False]
    expandedNodesStack = []
    visitedStates = []
    checkGoalState = initialState.copy()
    goalReached = False
    totalcost = 0

    #print("STARTING SEARCH WITH A DEPTH OF: ", depth)

    while (j < depth and goalReached == False):

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

        for state in expandedNodesStack:
            if state[2] == True and state[3] == True:
                goalReached = True
                checkGoalState = state
                

        if goalReached == False:
            if locater.checkHX2(currentState[0]) or locater.checkHX2(currentState[1]):
                if [currentState[0], currentState[1], currentState[2], True] in visitedStates:
                    pass
                else:
                    expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True])

            for state in expandedNodesStack:
                if state[2] == True and state[3] == True:
                    goalReached = True
                    checkGoalState = state


        #print("Possible States: ",  expandedNodesStack)
        #print("*" * 30)

        j = j + 1

    if goalReached == False:
        #print("GOAL NOT REACHED. RESTARTING SEARCH FROM BEGINNING")
        ID_Search(depth+1)
    else:
        #print("GOAL REACHED")
        print("Goal State Reached: ", checkGoalState)
        visitedStates.append(checkGoalState)

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
                
        print("Pathing: ")
        for state in visitedStates:
            if state == visitedStates[len(visitedStates)-1]:
                print(f"{state}")
            else:
                print(f"{state} -> ", end="")
        print("Total Cost: ", totalcost)
        print("Depth Reached: ", depth)

def UCS_Search():

    locater = Locations()
    HP = HarryPotter()
    AD = AlbusDumbledore()
    j = 0
    initialState = ["ln", "hw", False, False, 0]
    expandedNodesStack = []
    visitedStates = []
    treeRepresentation = {f"{initialState}": []}
    checkGoalState = initialState.copy()
    totalcost = 0
    lowestCost = False

    while checkGoalState[2] == False or checkGoalState[3] == False or lowestCost == False:
    #while j != 100:

        currentState = []

        travelPaths = {"HP": [], "AD": []}

        if j == 0:
            currentState = initialState.copy()
        else:
            currentState = expandedNodesStack.pop(0)
            treeRepresentation[f"{currentState}"] = []

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
                expandedNodesStack.append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3], currentState[4] + HP.move()])
                treeRepresentation[f"{currentState}"].append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3], currentState[4] + HP.move()])

        for i in range(len(travelPaths["AD"])):
            if [currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3], currentState[4] + AD.move()])
                treeRepresentation[f"{currentState}"].append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3], currentState[4] + AD.move()])

        if locater.checkHX1(currentState[0]) or locater.checkHX1(currentState[1]):
            if [currentState[0], currentState[1], True, currentState[3]] in visitedStates:
                pass
            else:
                if locater.checkHX1(currentState[0]):
                    expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3], currentState[4] + HP.dstryHX()])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], True, currentState[3], currentState[4] + HP.dstryHX()])
                else:
                    expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3], currentState[4] + AD.dstryHX()])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], True, currentState[3], currentState[4] + AD.dstryHX()])

        if locater.checkHX2(currentState[0]) or locater.checkHX2(currentState[1]):
            if [currentState[0], currentState[1], currentState[2], True] in visitedStates:
                pass
            else:
                if locater.checkHX2(currentState[0]):
                    expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True, currentState[4] + HP.dstryHX()])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], currentState[2], True, currentState[4] + HP.dstryHX()])
                else:
                    expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True, currentState[4] + AD.dstryHX()])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], currentState[2], True, currentState[4] + AD.dstryHX()])


        #print("Possible States: ",  expandedNodesStack)
        #print("*" * 30)
        def costSort(cost):
            return cost[4]

        expandedNodesStack.sort(key=costSort)

        #print("NODES SORTED BY COST: ")
        #print(expandedNodesStack)

        checkGoalState.clear()
        checkGoalState = currentState.copy()

        costCheck = False

        if checkGoalState[2] == True and checkGoalState[3] == True:
            for node in expandedNodesStack:
                if node[4] < checkGoalState[4]:
                    print("FOUND POSSIBLY CHEAPER PATH")
                    costCheck = True


        if costCheck != True:
            lowestCost = True

        j = j + 1

    print("Goal State Reached: ", checkGoalState)
            
    searchState = checkGoalState
    pathing = []
    
    while searchState != initialState:
        for i in range(len(visitedStates)):
            for j in range(len(treeRepresentation[f"{visitedStates[i]}"])):
                if treeRepresentation[f"{visitedStates[i]}"][j] == searchState:
                    pathing.insert(0, searchState)
                    searchState = visitedStates[i]

    pathing.insert(0, initialState)
    
    print("Pathing: ")
    for state in pathing:
        if state == pathing[len(pathing)-1]:
            print(f"{state}")
        else:
            print(f"{state} -> ", end="")

    for i in range(len(pathing)):
        if i == len(pathing)-1:
            pass
        elif pathing[i][0] != pathing[i+1][0]:
            totalcost += HP.move()
        elif pathing[i][1] != pathing[i+1][1]:
            totalcost += AD.move()
        elif pathing[i][2] != pathing[i+1][2]:
            if pathing[i+1][0] == "hm":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
        else:
            if pathing[i+1][0] == "gs":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()

    print("Total Cost: ", totalcost)

def A_STAR_Search():

    locater = Locations()
    HP = HarryPotter()
    AD = AlbusDumbledore()
    j = 0
    initialState = ["ln", "hw", False, False, 0]
    expandedNodesStack = []
    visitedStates = []
    treeRepresentation = {f"{initialState}": []}
    checkGoalState = initialState.copy()
    totalcost = 0
    lowestCost = False
    hValue = 0

    while checkGoalState[2] == False or checkGoalState[3] == False or lowestCost == False:
    #while j != 100:

        currentState = []

        travelPaths = {"HP": [], "AD": []}

        if j == 0:
            currentState = initialState.copy()
        else:
            currentState = expandedNodesStack.pop(0)
            treeRepresentation[f"{currentState}"] = []

        #print("*" * 30)
        #print("Current State: ", currentState)

        visitedStates.append(currentState)

        if currentState[3] == True and currentState[2] == True:
            hValue = 0
        elif (currentState[2] == True and currentState[3] == False) or (currentState[2] == False and currentState[3] == True):
            hValue = 1
        else:
            hValue = 2


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
                expandedNodesStack.append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3], currentState[4] + HP.move() + hValue])
                treeRepresentation[f"{currentState}"].append([travelPaths["HP"][i], currentState[1], currentState[2], currentState[3], currentState[4] + HP.move() + hValue])

        for i in range(len(travelPaths["AD"])):
            if [currentState[0], travelPaths["AD"][i], currentState[2], currentState[3]] in visitedStates:
                pass
            else:
                expandedNodesStack.append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3], currentState[4] + AD.move() + hValue])
                treeRepresentation[f"{currentState}"].append([currentState[0], travelPaths["AD"][i], currentState[2], currentState[3], currentState[4] + AD.move() + hValue])

        if locater.checkHX1(currentState[0]) or locater.checkHX1(currentState[1]):
            if [currentState[0], currentState[1], True, currentState[3]] in visitedStates:
                pass
            else:
                if locater.checkHX1(currentState[0]):
                    expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3], currentState[4] + HP.dstryHX() + 1])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], True, currentState[3], currentState[4] + HP.dstryHX() + 1])
                else:
                    expandedNodesStack.append([currentState[0], currentState[1], True, currentState[3], currentState[4] + AD.dstryHX() + 1])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], True, currentState[3], currentState[4] + AD.dstryHX() + 1])

        if locater.checkHX2(currentState[0]) or locater.checkHX2(currentState[1]):
            if [currentState[0], currentState[1], currentState[2], True] in visitedStates:
                pass
            else:
                if locater.checkHX2(currentState[0]):
                    expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True, currentState[4] + HP.dstryHX() + 1])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], currentState[2], True, currentState[4] + HP.dstryHX() + 1])
                else:
                    expandedNodesStack.append([currentState[0], currentState[1], currentState[2], True, currentState[4] + AD.dstryHX() + 1])
                    treeRepresentation[f"{currentState}"].append([currentState[0], currentState[1], currentState[2], True, currentState[4] + AD.dstryHX() + 1])


        #print("Possible States: ",  expandedNodesStack)
        #print("*" * 30)
        def costSort(cost):
            return cost[4]

        expandedNodesStack.sort(key=costSort)

        #print("NODES SORTED BY COST: ")
        #print(expandedNodesStack)

        checkGoalState.clear()
        checkGoalState = currentState.copy()

        costCheck = False

        if checkGoalState[2] == True and checkGoalState[3] == True:
            for node in expandedNodesStack:
                if node[4] < checkGoalState[4]:
                    print("FOUND POSSIBLY CHEAPER PATH")
                    costCheck = True


        if costCheck != True:
            lowestCost = True

        j = j + 1

    print("Goal State Reached: ", checkGoalState)
            
    searchState = checkGoalState
    pathing = []
    
    while searchState != initialState:
        for i in range(len(visitedStates)):
            for j in range(len(treeRepresentation[f"{visitedStates[i]}"])):
                if treeRepresentation[f"{visitedStates[i]}"][j] == searchState:
                    pathing.insert(0, searchState)
                    searchState = visitedStates[i]

    pathing.insert(0, initialState)
    
    print("Pathing: ")
    for state in pathing:
        if state == pathing[len(pathing)-1]:
            print(f"{state}")
        else:
            print(f"{state} -> ", end="")

    for i in range(len(pathing)):
        if i == len(pathing)-1:
            pass
        elif pathing[i][0] != pathing[i+1][0]:
            totalcost += HP.move()
        elif pathing[i][1] != pathing[i+1][1]:
            totalcost += AD.move()
        elif pathing[i][2] != pathing[i+1][2]:
            if pathing[i+1][0] == "hm":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()
        else:
            if pathing[i+1][0] == "gs":
                totalcost += HP.dstryHX()
            else:
                totalcost += AD.dstryHX()

    print("Total Cost: ", totalcost)

print("*" * 200)
print()
print("DFS SEARCH: ")
DFS_Search()
print()
print("*" * 200)

print()
print("BFS SEARCH: ")
BFS_Search()
print()
print("*" * 200)

print()
print("ITERATIVE DEEPENING SEARCH: ")
ID_Search()
print()
print("*" * 200)

print()
print("UNIFORM COST SEARCH: ")
UCS_Search()
print()
print("*" * 200)

print()
print("A* SEARCH: ")
A_STAR_Search()
print()
print("*" * 200)

