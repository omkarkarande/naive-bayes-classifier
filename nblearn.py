import sys
from NB import NB

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv) != 3:
        print("usage: python3 nblearn.py TRAININGFILE MODELFILE")
        sys.exit(0)
        
    naive_bayes = NB('TRAIN')
    naive_bayes.fit(sys.argv[1])
    naive_bayes.train()
    naive_bayes.generate_model(sys.argv[2])

if __name__ == "__main__":
    main()
