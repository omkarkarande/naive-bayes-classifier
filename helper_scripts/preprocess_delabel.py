import sys

#-----------------------------------------------------#
#Remove labels from the Training file passed as arg
#-----------------------------------------------------#
def process(ip, op):
    op_file = open(op, 'w')
    with open(ip, 'r') as f:
        for line in f:
            line = line.strip().split()
            #write back the line as it is stripping the first item
            line = line[1:]
            op_file.write(' '.join(map(str, line)) + '\n')

    op_file.close()
    return

#MAIN
def main():

    if len(sys.argv) != 3:
        print("USAGE: python3 process_delabel.py INPUT OUTPUT")
        sys.exit(0)

    process(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
