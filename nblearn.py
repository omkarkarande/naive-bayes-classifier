import sys
from NB import NB

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv) != 4:
        print("usage: python3 nblearn.py TRAININGFILE MODELFILE VOCAB")
        sys.exit(0)

    TRAIN_FILE = sys.argv[1]
    MODEL_FILE = sys.argv[2]

    #Change This Later
    VOCAB_FILE = sys.argv[3]
    LABELS = ['NEGATIVE', 'POSITIVE']
    #......................

    naive_bayes = NB()
    naive_bayes.fit(LABELS, VOCAB_FILE, TRAIN_FILE)
    naive_bayes.train(True)
    naive_bayes.generate_model(MODEL_FILE)

if __name__ == "__main__":
    main()
