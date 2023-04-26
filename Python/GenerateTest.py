import random

# DEFINE PARAMETER HERE
NUM_TESTCASE = 1
CAPACITY = 1500
NUM_ITEM = 36
NUM_CLASS = 5

# RANDOM HERE
for FileParameter in range(0, NUM_TESTCASE):
    filename = "INPUT_" + str(FileParameter) + ".TXT"
    file = open(filename, "w")

    file.write(str(CAPACITY) + "\n")
    file.write(str(NUM_CLASS) +"\n")

    for i in range(0, NUM_ITEM):
        if (i != NUM_ITEM - 1):
            file.write(str(random.randint(0, CAPACITY / 2)) + ", ")
        else:
            file.write(str(random.randint(0, CAPACITY / 2)) + "\n")

    for i in range(0, NUM_ITEM):
        if (i != NUM_ITEM - 1):
            file.write(str(random.randint(0, 100)) + ", ")
        else:
            file.write(str(random.randint(0, 100)) + "\n")

    for i in range(0, NUM_ITEM):
        if (i != NUM_ITEM - 1):
            file.write(str(random.randint(1, NUM_CLASS)) + ", ")
        else:
            file.write(str(random.randint(1, NUM_CLASS)))