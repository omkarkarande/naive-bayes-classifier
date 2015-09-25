import sys, os

def process(ip, op, vocab):
    VOCAB = []
    #read the vocabulary
    with open(vocab, 'r', encoding='latin1') as f:
        for line in f:
            VOCAB.append(line.strip())

    COUNTS = [0] * len(VOCAB)

    op_file = open(op, 'w')
    for root, dirs, files in os.walk(ip):
        for x in files:

    return

def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 preprocessor.py INPUT OUTPUT VOCAB")
        sys.exit(0)

    process(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
