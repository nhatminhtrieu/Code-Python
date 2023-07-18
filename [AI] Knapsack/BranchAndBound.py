def BranchAndBound(data, Result):
    Pos = []
    AvgArr = []

    for i in range(0, len(data.value)):
        Pos.append(i)
        AvgArr.append(data.value[i] / data.weight[i])

    # Sort all of them together base on AvgArr
    Zipped = zip(Pos, AvgArr, data.value, data.weight, data.label)
    SortedData = sorted(Zipped, key = lambda x : x[1], reverse = True)
    Pos, AvgArr, data.value, data.weight, data.label = zip(*SortedData)

    for x in range(0, len(data.value)):
        avg = 0

        if (x != len(data.value) - 1):
            avg = data.value[x + 1] / data.weight[x + 1]

        ValueWithoutX = data.CalcHeuristic(Result) + (data.capacity - data.CalcWeight(Result)) * avg

        Result[x] = 1
        if (data.CalcWeight(Result) <= data.capacity):
            ValueWithX = data.CalcHeuristic(Result) + (data.capacity - data.CalcWeight(Result)) * avg

            if (ValueWithoutX > ValueWithX):
                Result[x] = 0
        else:
            Result[x] = 0

    # Sort all of them base on original position
    Zipped = zip(Pos, Result, data.value, data.weight, data.label)
    SortedData = sorted(Zipped, key = lambda x : x[0])
    Pos, NewResult, data.value, data.weight, data.label = zip(*SortedData)

    Result.clear()
    for i in range(0, len(NewResult)):
        Result.append(NewResult[i])

    if (not data.InAllClass(Result)):
        Result.clear()
        for i in range(0, len(data.value)):
            Result.append(0)
   


def BranchAndBound_Main(data, FileParameter):
    Result = [0] * len(data.value)

    BranchAndBound(data, Result)

    data.WriteResult(FileParameter, Result)