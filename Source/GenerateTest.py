import random

# DEFINE PARAMETER HERE
CAPACITY = 5000
#NUM_ITEM = [10, 20, 25, 30, 40] # Use this for BF
NUM_ITEM = [50, 100, 200, 500, 1000] # Use this for the others
NUM_CLASS = 5

# RANDOM HERE
for FileParameter in range(0, len(NUM_ITEM)):
    filename = "INPUT_" + str(FileParameter) + ".TXT"
    file = open(filename, "w")

    file.write(str(CAPACITY) + "\n")
    file.write(str(NUM_CLASS) +"\n")

    num_item = NUM_ITEM[FileParameter]

    for i in range(0, num_item):
        if (i != num_item - 1):
            file.write(str(random.uniform(1, CAPACITY / 2)) + ", ")
        else:
            file.write(str(random.uniform(1, CAPACITY / 2)) + "\n")

    for i in range(0, num_item):
        if (i != num_item - 1):
            file.write(str(random.randint(1, 100)) + ", ")
        else:
            file.write(str(random.randint(1, 100)) + "\n")

    for i in range(0, num_item):
        if (i != num_item - 1):
            file.write(str(random.randint(1, NUM_CLASS)) + ", ")
        else:
            file.write(str(random.randint(1, NUM_CLASS)))