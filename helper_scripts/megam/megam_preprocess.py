import sys
from collections import defaultdict, OrderedDict

#MAIN
def main():

    if len(sys.argv) != 3:
        print("USAGE: python3 megam_preprocess.py INPUT OUTPUT")
        sys.exit(0)

    op_file = open(sys.argv[2], 'w')

    with open(sys.argv[1], 'r') as f:
        for line in f:
            #FEAT = defaultdict()
            line = line.strip().split()

            if line[0] =='POSITIVE' or line[0] == 'SPAM':
                line[0] = '1'
            else:
                line[0] = '0'


            op_file.write(' '.join(line).replace(':', ' ') + '\n')
            """
            for i in range(1, len(line)):
                feature = line[i].split(':')
                FEAT[int(feature[0])] = int(feature[1])


            #sort featres
            od = OrderedDict(sorted(FEAT.items()))
            for key, value in od.items():
                op_file.write(str(key) + ':' + str(value) + ' ')
            """
            #op_file.write('\n')

    op_file.close()


if __name__ == "__main__":
    main()
