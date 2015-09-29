import sys
from NB import NB

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv) != 3:
        print("usage: python3 nbclassify.py MODELFILE TESTFILE")
        sys.exit(0)

    #Create an instance of Naive Bayes class in classification mode
    naive_bayes = NB('CLASSIFY')
    #Load the model file into the class
    naive_bayes.load(sys.argv[1])
    #Get the predictions from the classifier
    predictions = naive_bayes.classify(sys.argv[2])

    #print out the predictions to stdout
    for prediction in predictions:
        print(prediction)



if __name__ == "__main__":
    main()
