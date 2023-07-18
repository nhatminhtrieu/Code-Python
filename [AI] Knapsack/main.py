from ClassData import DATA
from BruteForce import BruteForce_Main
from Genetic import Genetic_Main
from Beam import LocalBeam_Main
from BranchAndBound import BranchAndBound_Main



def main():
    data = DATA()
    FileParameter = 0

    while 1:
        if (data.ReadFile(FileParameter) == 0):
            exit()
        
        # Call Searching Algorithm Here
        #BruteForce_Main(data, FileParameter)
        Genetic_Main(data, FileParameter)
        #LocalBeam_Main(data, FileParameter)
        #BranchAndBound_Main(data, FileParameter)
        
        FileParameter += 1



main()