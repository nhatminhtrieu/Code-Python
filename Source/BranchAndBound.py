def BranchAndBound(data, Result):
    Pos = []
    AvgArr = []

    for i in range(data.Size()):
        Pos.append(i)
        AvgArr.append(data.m_Value[i] / data.m_Weight[i])

    # Sort all of them together base on AvgArr
    Zipped = zip(Pos, AvgArr, data.m_Value, data.m_Weight, data.m_Label)
    SortedData = sorted(Zipped, key = lambda x : x[1], reverse = True)
    Pos, AvgArr, data.m_Value, data.m_Weight, data.m_Label = zip(*SortedData)

    AvgArr = list(AvgArr)
    AvgArr.append(0)

    for x in range(0, data.Size()):
        ValueWithoutX = data.CalcValue(Result) + (data.Capacity() - data.CalcWeight(Result)) * AvgArr[x + 1]

        Result[x] = 1
        if (data.CalcWeight(Result) <= data.Capacity()):
            ValueWithX = data.CalcValue(Result) + (data.Capacity() - data.CalcWeight(Result)) * AvgArr[x + 1]

            if (ValueWithoutX > ValueWithX):
                Result[x] = 0
        else:
            Result[x] = 0

    # Sort all of them base on original position
    Zipped = zip(Pos, Result, data.m_Value, data.m_Weight, data.m_Label)
    SortedData = sorted(Zipped, key = lambda x : x[0])
    Pos, NewResult, data.m_Value, data.m_Weight, data.m_Label = zip(*SortedData)

    Result.clear()
    for i in range(0, len(NewResult)):
        Result.append(NewResult[i])

    if (not data.InAllClass(Result)):
        Result.clear()
        for i in range(0, data.Size()):
            Result.append(0)
   


def BranchAndBound_Main(data, FileParameter):
    Result = [0] * data.Size()

    BranchAndBound(data, Result)

    data.WriteResult(FileParameter, Result)