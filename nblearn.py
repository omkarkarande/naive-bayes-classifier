import sys
from NB import NB

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv) != 3:
        print("usage: python3 nblearn.py TRAININGFILE MODELFILE")
        sys.exit(0)

    #Create an instance of Naive Bayes class in training mode
    naive_bayes = NB('TRAIN')
    #Fit the data with the training file
    naive_bayes.fit(sys.argv[1])
    #Train the classifier
    naive_bayes.train()
    #Output a model file to the file specified
    naive_bayes.generate_model(sys.argv[2])

if __name__ == "__main__":
    main()
