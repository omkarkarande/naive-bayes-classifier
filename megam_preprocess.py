import sys
from collections import defaultdict, OrderedDict

#MAIN
def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 megam_preprocess.py INPUT OUTPUT INSERT_DUMMY_LABEL[1/0]")
        sys.exit(0)

    op_file = open(sys.argv[2], 'w')

    with open(sys.argv[1], 'r') as f:
        for line in f:
            #FEAT = defaultdict()
            line = line.strip().split()

            if int(sys.argv[3]) == 0:
                if line[0] =='POSITIVE' or line[0] == 'SPAM':
                    line[0] = '1'
                else:
                    line[0] = '0'
            else:
                #insert dummy label
                line = ['1'] + line
            #replace ':' with ' '
            op_file.write(' '.join(line).replace(':', ' ') + '\n')

    op_file.close()


if __name__ == "__main__":
    main()
