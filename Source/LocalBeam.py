# DEFINE MAX_K
MAX_K = 1000



def LocalBeam(data, BaseState, Result):
    if (len(BaseState) > MAX_K or len(BaseState) == 0):
        return
    
    NewState = list()

    for State in BaseState:
        IsResult = 1

        # The Pos is also true with State full of 0
        Pos = -1

        for i in range(data.Size() - 1, -1, -1): # data.Size() - 1 -> 0
            if (State[i] == 1):
                Pos = i
                break
                
        if (Pos + 1 <= data.Size() - 1):
            for i in range(Pos + 1, data.Size()):
                if (State[i] == 0):
                    # The successor's heuristic always larger than its predecessor
                    State[i] = 1

                    if (data.CalcWeight(State) > data.Capacity()):
                        State[i] = 0
                        break
                    else:
                        NewState.append(State.copy())
                        IsResult = 0
                    
                    State[i] = 0
            
            if (IsResult and data.InAllClass(State) 
                and data.CalcHeuristic(State) > data.CalcHeuristic(Result)):
                for i in range(data.Size()):
                    Result[i] = State[i]
    
    if (len(NewState) == 0):
        return
    
    NewState.sort(key = data.CalcHeuristic, reverse = True)
    del NewState[MAX_K:]

    BaseState.clear()
    
    for State in NewState:
        BaseState.append(State.copy())

    NewState.clear()

    LocalBeam(data, BaseState, Result)



def LocalBeam_Main(data, FileParameter):
    BaseState = []
    BaseState.append([0] * data.Size())
    Result = [0] * data.Size()
    Pos = []

    for i in range(data.Size()):
        Pos.append(i)

    Zipped = zip(Pos, data.m_Value, data.m_Weight, data.m_Label)
    SortedData = sorted(Zipped, key = lambda x : (x[2], -x[1]))
    Pos, data.m_Value, data.m_Weight, data.m_Label = zip(*SortedData)

    LocalBeam(data, BaseState, Result)

    Zipped = zip(Pos, Result, data.m_Value, data.m_Weight, data.m_Label)
    SortedData = sorted(Zipped, key = lambda x : x[0])
    Pos, Result, data.m_Value, data.m_Weight, data.m_Label= zip(*SortedData)
    Result = list(Result)

    data.WriteResult(FileParameter, Result) 