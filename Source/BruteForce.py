def BruteForce(data, BaseState, ResultState, index = 0):
    if (index >= len(BaseState)):
        return
    
    for k in range(2):
        BaseState[index] = k

        if (data.CalcWeight(BaseState) > data.Capacity()):
            BaseState[index] = 0
            return
        
        if (index == len(BaseState) - 1 and data.CalcValue(BaseState) > data.CalcValue(ResultState) and data.InAllClass(BaseState)):
            for i in range (len(BaseState)):
                ResultState[i] = BaseState[i]

        BruteForce(data, BaseState, ResultState, index + 1)
        
        BaseState[index] = 0

def BruteForce_Main(data, FileParameter):
    BaseState = [0] * data.Size()
    ResultState = [0] * data.Size()
    Pos = []

    for i in range(data.Size()):
        Pos.append(i)

    Zipped = zip(Pos, data.m_Value, data.m_Weight, data.m_Label)
    SortedData = sorted(Zipped, key = lambda x : (x[2], -x[1]))
    Pos, data.m_Value, data.m_Weight, data.m_Label = zip(*SortedData)

    BruteForce(data, BaseState, ResultState)

    Zipped = zip(Pos, ResultState, data.m_Value, data.m_Weight, data.m_Label)
    SortedData = sorted(Zipped, key = lambda x : x[0])
    Pos, ResultState, data.m_Value, data.m_Weight, data.m_Label = zip(*SortedData)
    ResultState = list(ResultState)

    data.WriteResult(FileParameter, ResultState)