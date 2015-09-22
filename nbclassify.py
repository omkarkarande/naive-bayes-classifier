import sys
from NB import NB

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv) != 3:
        print("usage: python3 nbclassify.py MODELFILE TESTFILE")
        sys.exit(0)

    MODELFILE = sys.argv[1]
    TESTFILE = sys.argv[2]

    naive_bayes = NB('CLASSIFY')
    naive_bayes.load(MODELFILE)
    predictions = naive_bayes.classify(TESTFILE)

    with open('predictions.out', 'w') as f:
        for prediction in predictions:
            f.write(prediction + '\n')



if __name__ == "__main__":
    main()
