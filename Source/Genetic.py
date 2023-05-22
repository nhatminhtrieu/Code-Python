import random
import sys
import math
from BranchAndBound import BranchAndBound

# INCREASE MAXIMUM RECURSION SIZE
sys.setrecursionlimit(1500)



# DEFINE GENETIC ALGORITHM'S VALUE
PopulationSize = 100
MutationRate = 0.2
MAX_DEPTH = 1000



def GeneratePopulation(data, BaseState):
    State = [0] * data.Size()
    BranchAndBound(data, State)
    BaseState.append(State.copy())
    
    for i in range(data.Size()):
        State[i] = 1
        BaseState.append(State.copy())
        State[i] = 0

    State.clear()

    for _ in range(PopulationSize * 100):
        State.clear()

        for _ in range(0, data.Size()):
            State.append(random.randint(0, 1))

        BaseState.append(State.copy())

    BaseState.sort(reverse = True, key = data.CalcFitness)
    del BaseState[PopulationSize:]



def FlipBit(x):
    if (x == 0):
        return 1
    else:
        return 0



def Genetic(data, BaseState, Depth):
    if (Depth >= MAX_DEPTH):
        return
    
    State = []
    count = 0

    for i in range(PopulationSize - 1):
        if (i == 0):
            NumLoop = math.ceil(PopulationSize / 2)
        else:
            NumLoop = random.randint(0, math.ceil(PopulationSize / 6))

        while (NumLoop != 0):
            NumLoop -= 1
            j = random.randint(i + 1, PopulationSize - 1)
            
            State.clear()
            count += 1

            #pos = random.randint(1, data.Size() - 1)
            pos = random.randint(int(data.Size() * 0.25), int(data.Size() * 0.75))

            State = BaseState[i][:pos] + BaseState[j][pos:]

            if (State not in BaseState and data.CalcWeight(State) <= data.Capacity()):
                BaseState.append(State.copy())

            if (count == PopulationSize):
                break

        if (count == PopulationSize):
            break

    
    BaseState.sort(reverse = True, key = data.CalcFitness)
    del BaseState[PopulationSize:]
    
    # Mutation
    for _ in range(math.ceil(MutationRate * len(BaseState))):
        i = random.randint(1, len(BaseState) - 1)
        State = BaseState[i].copy()
        k = random.randint(0, data.Size() - 1)
        State[k] = FlipBit(State[k])

        if (State not in BaseState and data.CalcWeight(State) <= data.Capacity()):
            BaseState[i][k] = FlipBit(BaseState[i][k])

    BaseState.sort(reverse = True, key = data.CalcFitness)

    Genetic(data, BaseState, Depth + 1)



def Genetic_Main(data, FileParameter):
    BaseState = list()
    GeneratePopulation(data, BaseState)

    Genetic(data, BaseState, 0)

    for State in BaseState:
        if (data.InAllClass(State) and data.CalcWeight(State) <= data.Capacity()):
            data.WriteResult(FileParameter, State)
            return
        
    data.WriteResult(FileParameter, [0] * data.Size())
    
    
