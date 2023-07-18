# DEFINE MAX_K
MAX_K = 1000



def LocalBeam(data, BaseState, Result):
    if (len(BaseState) > MAX_K or len(BaseState) == 0):
        return
    
    NewState = list()

    for State in BaseState:
        IsResult = 1
        for i in range(0, len(data.value)):
            if (State[i] == 0):
                # The successor's heuristic always larger than its predecessor
                State[i] = 1
            
                if (data.CalcWeight(State) <= data.capacity and State not in NewState):
                    NewState.append(State.copy())
                    IsResult = 0
                
                State[i] = 0
        
        if (IsResult):
            Result.append(State.copy())
    
    if (len(NewState) == 0):
        return
    
    BaseState.clear()
    
    for State in NewState:
        BaseState.append(State.copy())

    NewState.clear()

    BaseState.sort(reverse = True, key = data.CalcHeuristic)
    del BaseState[MAX_K:]

    LocalBeam(data, BaseState, Result)



def LocalBeam_Main(data, FileParameter):
    BaseState = []
    BaseState.append([0] * len(data.value))

    Result = []

    LocalBeam(data, BaseState, Result)
    Result.sort(reverse = True, key = data.CalcHeuristic)

    for State in Result:
        if (data.InAllClass(State)):
            data.WriteResult(FileParameter, State)
            return
        
    data.WriteResult(FileParameter, [0] * len(data.value))