import random



# DEFINE POPULATION SIZE
PopulationSize = 100



def GeneratePopulation(data, BaseState):
    State = []

    for k in range(0, PopulationSize):
        while 1:
            State.clear()
            for i in range(0, len(data.value)):
                State.append(random.randint(0, 1))
            if (data.CalcWeight(State) <= data.capacity):
                break
        BaseState.append(State.copy())

    BaseState.sort(reverse = True, key = data.CalcHeuristic)



def FlipBit(x):
    if (x == 0):
        return 1
    else:
        return 0



def Genetic(data, BaseState):
    OldBestState = BaseState[0]
    state = []
    count = 0

    for i in range(0, PopulationSize - 1):
        if (i == 0):
            NumLoop = int(PopulationSize / 2)
        else:
            NumLoop = random.randint(0, int(PopulationSize / 6))

        while (NumLoop != 0):
            NumLoop -= 1
            j = random.randint(i + 1, PopulationSize - 1)
            
            state.clear()
            count += 1

            pos = random.randint(1, len(data.value))

            state = BaseState[i][:pos] + BaseState[j][pos:]

            if (data.CalcWeight(state) <= data.capacity and state not in BaseState):
                BaseState.append(state.copy())

            if (count == PopulationSize):
                break

    
    BaseState.sort(reverse = True, key = data.CalcHeuristic)
    del BaseState[PopulationSize:]
    if (OldBestState == BaseState[0]):
        return
    
    # Mutation
    for x in range(0, int(0.02 * len(BaseState))):
        i = random.randint(1, len(BaseState) - 1)
        State = BaseState[i].copy()
        k = random.randint(0, len(data.value) - 1)
        State[k] = FlipBit(State[k])

        if (State not in BaseState and data.CalcWeight(State) <= data.capacity):
            BaseState[i][k] = FlipBit(BaseState[i][k])

    # BaseState.sort(reverse = True, key = data.CalcHeuristic)

    Genetic(data, BaseState)



def Genetic_Main(data, FileParameter):
    BaseState = list()
    GeneratePopulation(data, BaseState)

    Genetic(data, BaseState)

    for State in BaseState:
        if (data.InAllClass(State)):
            data.WriteResult(FileParameter, State)
            return
        
    data.WriteResult(FileParameter, [0] * len(data.value))