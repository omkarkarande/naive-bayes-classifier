import math
from collections import defaultdict

#################################
#Naive Bayes implementation
#################################
class NB:

    def __init__(self, mode):
        #Stores the probabilities of each word
        self.vocab_data = defaultdict()
        #Stores the probability of each label
        self.label_data = defaultdict()

        #Maps label indices to label meanings
        self.label_mapping = []
        #Stores the words in the vocab (debugging)
        if mode == 'TRAIN':
            self.vocab = []
            self.labels = []

        #Total label count
        self.label_count = 0
        #Entire size of the vocabulary
        self.vocab_size = 0

        self.words_per_label = []
        self.total_records = 0

        return

    def init_labels(self, dataset):
        #detect all labels from training data
        with open(dataset, 'r') as f:
            for line in f:
                line = line.strip().split()
                if line[0] not in self.labels:
                    self.labels.append(line[0])

        self.label_count = len(self.labels)
        self.words_per_label = [0] * self.label_count
        i = 0
        for label in self.labels:
            self.label_data[i] = 0.0
            self.label_mapping.append((i, label))
            i += 1

        return

    """
    def init_vocab(self, vocab_file):
        with open(vocab_file, 'r') as f:
            i = 1
            for line in f:
                self.vocab.append(line.strip())
                i += 1
        self.vocab_size = len(self.vocab)

        return
"""

    def fit(self, vocab, dataset):

        self.init_labels(dataset)
        #self.init_vocab(vocab)

        with open(dataset, 'r') as f:
            for line in f:
                self.total_records += 1
                line = line.strip().split()

                label = self.labels.index(line[0])
                line = line[1:]

                #label count
                self.label_data[label] += 1.0
                #go through the entire line
                for feature in line:
                    feature = feature.split(':')
                    if int(feature[0]) not in self.vocab_data.keys():
                        self.vocab_data[int(feature[0])] = [0.0] * self.label_count

                    self.vocab_data[int(feature[0])][label] += int(feature[1])
                    self.words_per_label[label] += int(feature[1])

        return

    def train(self, add_one):
        if add_one:
            for i in range(self.label_count):
                self.words_per_label[i] += len(self.vocab_data)

        #calculate the word probabilities
        for key, value in self.vocab_data.items():
            for i in range(self.label_count):
                value[i] = (value[i] + 1.0)/float(self.words_per_label[i]) if add_one else value[i]/float(self.words_per_label[i])

        #calculate label probabilities
        for key in self.label_data.keys():
            self.label_data[key] = self.label_data[key]/float(self.total_records)

        return

    def generate_model(self, model_file):
        with open(model_file, 'w') as f:
            #label count
            f.write('LABEL_COUNT:' + str(self.label_count) + '\n')
            #label mapping
            f.write('LABEL_MAPPING:' + str(self.label_mapping) + '\n')
            #label probabilities
            f.write('LABEL_PROBABILITIES:[')
            for i in range(self.label_count):
                if i != self.label_count - 1:
                    f.write(str(self.label_data[i]) + ', ')
                else:
                    f.write(str(self.label_data[i]) + ']\n')
            #token probabilities
            for key, value in self.vocab_data.items():
                f.write(str(key) + ":" + str(value) + '\n')

        return

    def load(self, model):
        #read from a model
        with open(model, 'r') as f:
            #read number of labels
            line = f.readline().strip().split(':')
            self.label_count = int(line[1])
            print(self.label_count)
            #read label mappings
            line = f.readline().strip().split(':')
            self.label_mapping = eval(line[1])
            print(self.label_mapping)
            #read label probabilities
            line = f.readline().strip().split(':')
            i=0
            for x in eval(line[1]):
                self.label_data[i] = float(x)
                i += 1
            print(self.label_data)
            #read vocab probabilities
            for line in f:
                line = line.strip().split(':')
                self.vocab_data[int(line[0])] = eval(line[1])
            print(self.vocab_data)
        return


    def P(self, message, label):
        prob = 0.0
        for feature in message:
            feature = feature.split(':')
            if int(feature[0]) in self.vocab_data.keys():
                prob += float(feature[1]) * math.log(self.vocab_data[int(feature[0])][label])

        return prob


    def classify(self, dataset):

        predictions = []
        with open(dataset, 'r') as f:
            for line in f:

                line = line.strip().split()
                LINE_PROBABILITY = [0.0] * self.label_count
                for i in range(self.label_count):
                    LINE_PROBABILITY[i] = math.log(self.label_data[i]) + self.P(line, i)

                MAX = LINE_PROBABILITY.index(max(LINE_PROBABILITY))
                print(LINE_PROBABILITY)
                for x in self.label_mapping:
                    if x[0] == MAX:
                        predictions.append(x[1])

        return predictions
