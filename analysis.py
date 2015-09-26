import sys


#------------------------------------------#
#Calculate the accuracy of the predictions
#------------------------------------------#
def accuracy_score(actual, predictions):
    correct = 0.0
    for i in range(len(actual)):
        if actual[i] == predictions[i]:
            correct += 1.0

    return correct / float(len(actual))

#--------------------------#
#Calculate the precision
#--------------------------#
def precision_score(actual, predictions):

    correct_pos = 0.0
    class_pos = 0.0
    correct_neg = 0.0
    class_neg = 0.0

    for i in range(len(actual)):
        if actual[i] == predictions[i] == 'POSITIVE':
            correct_pos += 1.0
        if actual[i] == predictions[i] == 'NEGATIVE':
            correct_neg += 1.0
        if predictions[i] == 'POSITIVE':
            class_pos += 1.0
        if predictions[i] == 'NEGATIVE':
            class_neg += 1.0

    return correct_pos/class_pos, correct_neg/class_neg

#--------------------------#
#Calculate the recall
#--------------------------#
def recall_score(actual, predictions):

    correct_pos = 0.0
    class_pos = 0.0
    correct_neg = 0.0
    class_neg = 0.0

    for i in range(len(actual)):
        if actual[i] == predictions[i] == 'POSITIVE':
            correct_pos += 1.0
        if actual[i] == predictions[i] == 'NEGATIVE':
            correct_neg += 1.0
        if actual[i] == 'POSITIVE':
            class_pos += 1.0
        if actual[i] == 'NEGATIVE':
            class_neg += 1.0

    return correct_pos/class_pos, correct_neg/class_neg

#--------------------------#
#Calculate the f1
#--------------------------#
def f1_score(precision, recall):
    return (2 * precision * recall) / (precision + recall)

#MAIN
def main():
    if len(sys.argv) != 3:
        print("USAGE: python3 analys.py <ACTUAL> <PREDICTIONS>")
        sys.exit(0)

    ACT = sys.argv[1]
    PRED = sys.argv[2]

    actual = []
    predictions = []

    with open(ACT, 'r') as f:
        for line in f:
            line = line.strip().split()
            actual.append(line[0])

    with open(PRED, 'r') as f:
        for line in f:
            line = line.strip()
            predictions.append(line)

    accuracy = accuracy_score(actual, predictions)
    precision_pos, precision_neg = precision_score(actual, predictions)
    recall_pos, recall_neg = recall_score(actual, predictions)
    f1_pos = f1_score(precision_pos, recall_pos)
    f1_neg = f1_score(precision_neg, recall_neg)

    print('ACCURACY: ' + str(accuracy * 100) + "%")
    print('PRECISION(pos): ' + str(precision_pos * 100) + '%')
    print('PRECISION(neg): ' + str(precision_neg * 100) + '%')
    print('RECALL(pos): ' + str(recall_pos * 100) + '%')
    print('RECALL(neg): ' + str(recall_neg * 100) + '%')
    print('F1(pos): ' + str(f1_pos))
    print('F1(neg): ' + str(f1_neg))

if __name__ == "__main__":
    main()
