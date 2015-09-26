import sys

#---------------------------------#
#Process the imdb files
#Label the dataset appropriately
#---------------------------------#
def process(ip, op):
    #open the input dataset
    op_file = open(op, 'w')
    with open(ip, 'r') as f:
        for line in f:
            line = line.strip().split()

            #POS NEG labeling
            if int(line[0]) >= 7:
                line[0] = 'POSITIVE'
            elif int(line[0]) <= 4:
                line[0] = 'NEGATIVE'

            #Normalize all the tokens to start from 1
            for x in range(1, len(line)):
                feature = line[x].split(':')
                feature[0] = int(feature[0]) + 1
                line[x] = ':'.join(map(str, feature))

            op_file.write(' '.join(map(str, line)) + '\n')

    op_file.close()
    return

#MAIN
def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 preprocessor.py INPUT OUTPUT")
        sys.exit(0)

    process(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
