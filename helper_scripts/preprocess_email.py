import sys, os
from collections import defaultdict

#---------------------------------------------------------------------#
#Generate a single file from all the email files given in the folder
#passed as the argument in ip
#---------------------------------------------------------------------#
def process(ip, op, vocab, testdata):
    
    VOCAB = defaultdict()
    #Read the vocabulary
    with open(vocab, 'r', encoding='latin1') as f:
        i = 1
        for line in f:
            #Map vocabulary to indices
            VOCAB[line.strip()] = [str(i), 0]
            i += 1


    op_file = open(op, 'w')
    for root, dirs, files in os.walk(ip):
        #For all files in the give directory
        if testdata:
            files = sorted(files)

        for x in files:
            print('Processing: ' + x)

            if not testdata:
                #Check for SPAM or HAM file
                if 'spam' in x:
                    op_file.write('SPAM ')
                elif 'ham' in x:
                    op_file.write('HAM ')
                else:
                    #Do not Process other files
                    print('Skiping File: ' + x)
                    continue

            #Open each file
            with open(root + '/' + x, 'r', encoding='latin1') as f:
                for line in f:
                    line = line.strip().split()
                    #Count tokens
                    for word in line:
                        VOCAB[word][1] += 1

            #Write to File
            for key, value in VOCAB.items():
                if value[1] != 0:
                    op_file.write(value[0] + ':' + str(value[1]) + ' ')
                    #reset for the next file
                    VOCAB[key][1] = 0

            #Write a new line
            op_file.write('\n')

    op_file.close()
    return

def main():

    if len(sys.argv) != 5:
        print("USAGE: python3 preprocessor.py INPUT OUTPUT VOCAB LABELED/UNLABELED[1/0]")
        sys.exit(0)

    if int(sys.argv[4]) == 1:
        process(sys.argv[1], sys.argv[2], sys.argv[3], False)
    else:
        process(sys.argv[1], sys.argv[2], sys.argv[3], True)

if __name__ == "__main__":
    main()
