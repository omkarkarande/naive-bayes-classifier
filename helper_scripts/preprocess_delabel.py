import sys

def remove_labels(ip, op):
    op_file = open(op, 'w')
    with open(ip, 'r') as f:
        for line in f:
            line = line.strip().split()
            line = line[1:]
            op_file.write(' '.join(map(str, line)) + '\n')

    op_file.close()
    return

def main():

    if len(sys.argv) != 4:
        print("USAGE: python3 preprocessor.py INPUT OUTPUT")
        sys.exit(0)

    process(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
