import sys

def processIMDB(ip, op):
    #open the input dataset
    op_file = open(op, 'w')
    with open(ip, 'r') as f:
        for line in f:
            line = line.strip().split()

            if int(line[0]) >= 7:
                line[0] = 1
            elif int(line[0]) <= 4:
                line[0] = 0

            for x in range(1, len(line)):
                feature = line[x].split(':')
                feature[0] = int(feature[0]) + 1
                line[x] = ':'.join(map(str, feature))

            op_file.write(' '.join(map(str, line)) + "\n")

    op_file.close()


def processEMAIL(ip, op):
    return


def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 preprocessor.py INPUTFILE OUTPUTFILE DATATYPE")
        sys.exit(0)


    INPUT = sys.argv[1]
    OUTPUT = sys.argv[2]
    TYPE = sys.argv[3]

    if TYPE == 'imdb':
        processIMDB(INPUT, OUTPUT)
    elif TYPE == 'email':
        processEMAIL(INPUT, OUTPUT)
    else:
        print("Invalid TYPE. Use 'imdb' / 'email'")
        sys.exit(1)

if __name__ == "__main__":
    main()
