import os

class DATA:
    # ==================== Initialize ====================
    def __init__(self, Capacity, NumClass, arr0, arr1, arr2):
        self.m_Capacity = Capacity
        self.m_NumClass = NumClass

        self.m_Weight = arr0
        self.m_Value = arr1
        self.m_Label = arr2



    def __init__(self):
        self.m_Capacity = 0
        self.m_NumClass = 0

        self.m_Weight = []
        self.m_Value = []
        self.m_Label = []

    # ==================== Get Class Value ====================
    def Size(self):
        return len(self.m_Value)
    
    def Capacity(self):
        return self.m_Capacity

    # ==================== Calculate Function ====================
    def CalcValue(self, State):
        if (len(State) == 0):
            return 0
        
        res = 0

        for i in range(len(State)):
            res += State[i] * self.m_Value[i]

        return res
        


    def CalcWeight(self, State):
        if (len(State) == 0):
            return 0
        
        res = 0

        for i in range(len(State)):
            res += State[i] * self.m_Weight[i]

        return res
    


    def CalcHeuristic(self, State):
        return self.CalcValue(State)
    


    def CalcFitness(self, State):
        if (self.CalcWeight(State) > self.m_Capacity):
            return 0
        return self.CalcValue(State)
    
    # ==================== Check if 'State' has all class ====================
    def InAllClass(self, State):
        # Class No. start from 1 => flag[0] is useless
        flag = [0] * (self.m_NumClass + 1)

        for i in range(len(State)):
            if (State[i] == 1):
                flag[self.m_Label[i]] = 1

        for i in range(1, self.m_NumClass + 1):
            if (flag[i] == 0):
                return 0
            
        return 1
    
    # ==================== Read/Write File ====================
    def ReadFile(self, FileParameter):
        filename = "INPUT_" + str(FileParameter) + ".TXT"
        if os.path.exists(filename) == 0:
            return 0

        file = open(filename, "r")
        self.m_Capacity = float(file.readline())
        self.m_NumClass = int(file.readline())
        arr = []
        
        for i in range(3):
            line = file.readline()
            if (i != 0):
                arr.append([int(x) for x in line.split(',')])
            else:
                arr.append([float(x) for x in line.split(',')])

        self.m_Weight = arr[0]
        self.m_Value = arr[1]
        self.m_Label = arr[2]

        file.close()
        return 1



    def WriteResult(self, FileParameter, State):
        filename = "OUTPUT_" + str(FileParameter) + ".TXT"
        file = open(filename, "w")

        file.write(str(self.CalcHeuristic(State)) + "\n")

        file.write(", ".join([str(x) for x in State]))
