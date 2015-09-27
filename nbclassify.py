import sys
from NB import NB

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv) != 3:
        print("usage: python3 nbclassify.py MODELFILE TESTFILE")
        sys.exit(0)

    naive_bayes = NB('CLASSIFY')
    naive_bayes.load(sys.argv[1])
    predictions = naive_bayes.classify(sys.argv[2])

    for prediction in predictions:
        print(prediction)



if __name__ == "__main__":
    main()
