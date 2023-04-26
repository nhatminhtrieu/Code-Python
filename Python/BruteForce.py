def BruteForce(data, BaseState, ResultState, index = 0):
    if (index >= len(BaseState)):
        return
    
    for k in range(0, 2):
        BaseState[index] = k

        if (index == len(BaseState) - 1 and data.CalcHeuristic(BaseState) > data.CalcHeuristic(ResultState) 
            and data.CalcWeight(BaseState) <= data.capacity and data.InAllClass(BaseState)):
            for i in range (0, len(BaseState)):
                ResultState[i] = BaseState[i]

        BruteForce(data, BaseState, ResultState, index + 1)

def BruteForce_Main(data, FileParameter):
    BaseState = [0] * len(data.value)
    ResultState = [0] * len(data.value)
    
    BruteForce(data, BaseState, ResultState)

    data.WriteResult(FileParameter, ResultState)