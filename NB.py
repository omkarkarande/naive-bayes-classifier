from collections import defaultdict

#################################
#Naive Bayes implementation
#################################
class NB:

    def __init__(self):
        #Stores the probabilities of each word
        self.vocab_data = defaultdict()
        #Stores the probability of each label
        self.label_data = defaultdict()

        #Maps label indices to label meanings
        self.label_mapping = []
        #Stores the words in the vocab (debugging)
        self.vocab = []

        #Total label count
        self.label_count = 0
        #Entire size of the vocabulary
        self.vocab_size = 0

        self.words_per_label = []
        self.total_records = 0

        self.was_add_one_used = False
        return


    def init_labels(self, label_list):
        self.label_count = len(label_list)
        self.words_per_label = [0] * self.label_count
        i = 0
        for label in label_list:
            self.label_data[i] = 0.0
            self.label_mapping.append((i, label))
            i += 1

        return


    def init_vocab(self, vocab_file):
        with open(vocab_file, 'r') as f:
            i = 1
            for line in f:
                self.vocab.append(line.strip())
                self.vocab_data[i] = [0.0] * self.label_count
                i += 1
        self.vocab_size = len(self.vocab)

        return


    def fit(self, labels, vocab, dataset):

        self.init_labels(labels)
        self.init_vocab(vocab)

        with open(dataset, 'r') as f:
            for line in f:
                self.total_records += 1
                line = line.strip().split()

                label = int(line[0])
                line = line[1:]

                #label count
                self.label_data[label] += 1.0
                #go through the entire line
                for feature in line:
                    feature = feature.split(':')
                    self.vocab_data[int(feature[0])][label] += int(feature[1])
                    self.words_per_label[label] += int(feature[1])

        return

    def train(self, add_one):
        self.was_add_one_used = add_one
        if add_one:
            for i in range(self.label_count):
                self.words_per_label[i] += self.vocab_size

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
            #records parsed
            f.write('TRAINING_RECORDS:' + str(self.total_records) + '\n')
            #Add one
            f.write('ADD_ONE:True\n') if self.was_add_one_used else f.write('ADD_ONE:False\n')
            #vocab size
            f.write('VOCAB_SIZE:' + str(self.vocab_size) + '\n')
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

    def classify():
        return
