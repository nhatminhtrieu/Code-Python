import os

class DATA:
    def __init__(self, Capacity, NumClass, arr0, arr1, arr2):
        self.capacity = Capacity
        self.numClass = NumClass

        self.weight = arr0
        self.value = arr1
        self.label = arr2

    def __init__(self):
        self.capacity = 0
        self.numClass = 0

        self.weight = []
        self.value = []
        self.label = []
    
    def CalcHeuristic(self, arr):
        if (len(arr) == 0):
            return 0
        
        res = 0

        for index in range(0, len(arr)):
            res += arr[index] * self.value[index]

        return res
    
    def CalcWeight(self, arr):
        res = 0

        for index in range(0, len(arr)):
            res += arr[index] * self.weight[index]

        return res
    
    def InAllClass(self, state):
        # Class No. start from 1 => flag[0] is useless
        flag = [0] * (self.numClass + 1)

        for i in range(0, len(state)):
            if (state[i] == 1):
                flag[self.label[i]] = 1

        for i in range(1, self.numClass + 1):
            if (flag[i] == 0):
                return 0
            
        return 1
    
    def ReadFile(self, FileParameter):
        filename = "INPUT_" + str(FileParameter) + ".TXT"
        if os.path.exists(filename) == 0:
            return 0

        file = open(filename, "r")
        self.capacity = int(file.readline())
        self.numClass = int(file.readline())
        arr = []

        for index in range(0, 3):
            line = file.readline()
            arr.append([int(x) for x in line.split(',')])

        self.weight = arr[0]
        self.value = arr[1]
        self.label = arr[2]

        file.close()
        return 1

    def WriteResult(self, FileParameter, state):
        filename = "OUTPUT_" + str(FileParameter) + ".TXT"
        file = open(filename, "w")

        file.write(str(self.CalcHeuristic(state)) + "\n")

        file.write(str(state))
        
