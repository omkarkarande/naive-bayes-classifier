import sys

def main():

    if len(sys.argv) != 4:
        print('USAGE: python3 stats.py <FILE> <LABELS> <FEATURE>')
        sys.exit(0)

    FILE = sys.argv[1]
    LABELS = sys.argv[2].strip().split(',')
    FEATURE = sys.argv[3]

    LABEL_COUNT = [0, 0]
    FEATURE_COUNT = [0, 0]

    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip().split()

            label = line[0]

            if label == LABELS[0]:
                LABEL_COUNT[0] += 1
            elif label == LABELS[1]:
                LABEL_COUNT[1] += 1

            line = line[1:]
            for features in line:
                feature = features.split(':')
                if feature[0] == FEATURE:
                    if label == LABELS[0]:
                        FEATURE_COUNT[0] += int(feature[1])
                    else:
                        FEATURE_COUNT[1] += int(feature[1])


    print(LABEL_COUNT)
    print(FEATURE_COUNT)

if __name__ == "__main__":
    main()
