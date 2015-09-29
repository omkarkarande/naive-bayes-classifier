import sys, random

#MAIN
def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 data_partitioner.py <DATASET> <TRAINING PERCENT> <UNIFORM/RANDOM: 1/0>")
        sys.exit(0)

    DATASET = sys.argv[1];
    TRAIN_PERC = int(sys.argv[2])
    UNIFORM = int(sys.argv[3])

    #read the dataset line by line into a list
    data = []
    with open(DATASET, "r") as f:
        for line in f:
            data.append(line.strip())

    LEN = len(data)

    #lists to store training and testing data
    train_data = []
    test_data = []

    #Where to split the data based on percentage passed in the argument
    SPLIT_POINT = int(LEN * TRAIN_PERC / 100)
    if UNIFORM != 1:
        #Shuffle the dataset randomly
        random.shuffle(data)

    train_data = data[:SPLIT_POINT]
    test_data = data[SPLIT_POINT:]


    #write the data out to a file
    #Naming convention TRAIN(percentvalue).feat
    with open("TRAIN" + str(TRAIN_PERC) + ".feat", "w") as f:
        for item in train_data:
            f.write(str(item) + "\n")

    #write the data out to a file
    #Naming convention TEST(percentvalue).feat
    with open("TEST" + str(100 - TRAIN_PERC) + ".feat", "w") as f:
        for item in test_data:
            f.write(str(item) + "\n")


if __name__ == "__main__":
    main()
