import sys

def main():

    #Simple argument consistency check
    #Exit if arguments not specified
    if len(sys.argv != 3):
        print("usage: python3 nblearn.py MODELFILE TESTFILE")
        sys.exit(0)


if __name__ == "__main__":
    main()
