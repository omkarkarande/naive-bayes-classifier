import sys

#MAIN
def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 megam_postprocess.py INPUT OUTPUT TYPE")
        sys.exit(0)

    op_file = open(sys.argv[2], 'w')
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip().split()

            #Check the first item in each line if it is 1 or 0
            if float(line[0]) == 1:
                if sys.argv[3] == 'imdb':
                    line = 'POSITIVE'
                elif sys.argv[3] == 'enron':
                    line = 'SPAM'
            else:
                if sys.argv[3] == 'imdb':
                    line = 'NEGATIVE'
                elif sys.argv[3] == 'enron':
                    line = 'HAM'
            #write out the line to output file
            op_file.write(line + '\n')

    op_file.close()


if __name__ == "__main__":
    main()
