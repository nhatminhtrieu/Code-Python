from ClassData import DATA
from BruteForce import BruteForce_Main
from Genetic import Genetic_Main
from LocalBeam import LocalBeam_Main
from BranchAndBound import BranchAndBound_Main
from timeit import default_timer as timer
import sys



def main():
    # Arguments' help
    if (len(sys.argv) == 1):
        print("Instruction:")
        print("     Type '-bf' for Brute Force")
        print("     Type '-bb' for Branch and Bound")
        print("     Type '-lb' for Local Beam Search")
        print("     Type '-ge' for Genetic Algorithm")
        exit()

    # Assign algorithm
    Algorithm = 0

    if (sys.argv[1] == "-bf"):
        Algorithm = BruteForce_Main
    elif (sys.argv[1] == "-bb"):
        Algorithm = BranchAndBound_Main
    elif (sys.argv[1] == "-ge"):
        Algorithm = Genetic_Main
    elif (sys.argv[1] == "-lb"):
        Algorithm = LocalBeam_Main
    else:
        print("Invalid argument")
        exit()
        
    # Running algorithm
    data = DATA()
    FileParameter = 0

    while 1:
        if (data.ReadFile(FileParameter) == 0):
            exit()
        
        TimeStart = timer()
        Algorithm(data, FileParameter)
        TimeEnd = timer()

        print("Running Time:", TimeEnd - TimeStart)
        
        FileParameter += 1



main()