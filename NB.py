import math
from collections import defaultdict

#################################
#Naive Bayes implementation
#################################
class NB:

    #-----------------------------#
    #Initializer for Naive Bayes
    #-----------------------------#
    def __init__(self, mode):
        #Stores the probabilities of each word
        self.vocab_data = defaultdict()
        #Stores the probability of each label
        self.label_data = defaultdict()

        #Maps label indices to label meanings
        #Stores tuples in the format (identifier, string)
        self.label_mapping = []
        #Total label count
        self.label_count = 0


        #Stores the words in the vocab (debugging)
        if mode == 'TRAIN':
            #stores the lables in the training file
            self.labels = []
            #stores the word count per label
            self.words_per_label = []
            self.total_records = 0

        return

    #-------------------------------------------------#
    #Retrives the reverse mapping for the labels.
    #Maps label string to unique identifier
    #-------------------------------------------------#
    def get_reverse_mapping(self, label):
        for x in self.label_mapping:
            if x[1] == label:
                return x[0]

    #Initialize the labels for the instance of bayes.
    def init_labels(self, dataset):
        #detect all labels from training data
        with open(dataset, 'r') as f:
            for line in f:

                #breaking condition for 2 labels            #REMEMBER THIS
                if len(self.labels) == 2:
                    break

                line = line.strip().split()
                #If encounters a new label, puts it in the list
                if line[0] not in self.labels:
                    self.labels.append(line[0])

        #Initialize label_count
        self.label_count = len(self.labels)
        #Initialize words_per_label
        self.words_per_label = [0] * self.label_count

        #Set up label mappings
        i = 0
        for label in self.labels:
            self.label_data[i] = 0.0
            self.label_mapping.append((i, label))
            i += 1

        return

    #--------------------------------------------------------#
    #Fits the classifier with training data
    #Stores in all the counts of unique tokens and labels
    #--------------------------------------------------------#
    def fit(self, dataset):

        #Initializes labels
        self.init_labels(dataset)

        with open(dataset, 'r') as f:
            for line in f:
                #Count the number of records in the training set
                self.total_records += 1
                line = line.strip().split()

                #Get label identifier
                label = self.get_reverse_mapping(line[0])
                #Strip the line of the label
                line = line[1:]

                #Count the occurance of the identified label
                self.label_data[label] += 1.0
                #Parse the line to extract features
                for feature in line:
                    feature = feature.split(':')
                    #If token not in the vocabulary, add it to the vocabulary
                    if int(feature[0]) not in self.vocab_data.keys():
                        #Initialize the probabilities for the token
                        self.vocab_data[int(feature[0])] = [0.0] * self.label_count

                    #Count the occurance of the identified token
                    self.vocab_data[int(feature[0])][label] += int(feature[1])
                    #Increment the word count for the label by the token count
                    self.words_per_label[label] += int(feature[1])

        return

    #--------------------------------------------------------------#
    #Trains the classifier based on the fitted training data
    #--------------------------------------------------------------#
    def train(self):

        #calculate the word probabilities
        for key, value in self.vocab_data.items():
            for i in range(self.label_count):
                #Using add-one smoothing
                value[i] = (value[i] + 1) / (self.words_per_label[i] + len(self.vocab_data))

        #calculate label probabilities
        for key in self.label_data.keys():
            self.label_data[key] = self.label_data[key]/float(self.total_records)

        return

    #---------------------------------------------------#
    #Generates a model file based on the trained data
    #Stores it in the filename passed as args
    #---------------------------------------------------#
    def generate_model(self, model_file):
        with open(model_file, 'w') as f:

            #Write label count to the file
            f.write('LABEL_COUNT:' + str(self.label_count) + '\n')

            #Write label mapping to the file
            f.write('LABEL_MAPPING:' + str(self.label_mapping) + '\n')

            #Write label probabilities to the file
            f.write('LABEL_PROBABILITIES:[')
            for i in range(self.label_count):
                #For not printing space after the last entry
                if i != self.label_count - 1:
                    f.write(str(self.label_data[i]) + ', ')
                else:
                    f.write(str(self.label_data[i]) + ']\n')

            #Write token probabilities to the file
            for key, value in self.vocab_data.items():
                f.write(str(key) + ":" + str(value) + '\n')

        return

    #----------------------------------------------#
    #Loads in the data from the given model file
    #Used for classification
    #----------------------------------------------#
    def load(self, model):
        #Read from the given model file
        with open(model, 'r') as f:
            #Read number of labels
            line = f.readline().strip().split(':')
            self.label_count = int(line[1])

            #Read label mappings
            line = f.readline().strip().split(':')
            self.label_mapping = eval(line[1])

            #Read label probabilities
            line = f.readline().strip().split(':')
            i=0
            for x in eval(line[1]):
                self.label_data[i] = float(x)
                i += 1

            #read vocab probabilities
            for line in f:
                line = line.strip().split(':')
                self.vocab_data[int(line[0])] = eval(line[1])

        return

    #--------------------------------------------------------------------------------#
    #Conditional Probability
    #Returns sum of log of probabilities of all tokens in the given featureset
    #--------------------------------------------------------------------------------#
    def P(self, message, label):
        prob = 0.0
        for feature in message:
            feature = feature.split(':')
            if int(feature[0]) in self.vocab_data.keys():
                prob += float(feature[1]) * math.log(self.vocab_data[int(feature[0])][label])

        return prob

    #-----------------------------------------------------#
    #Predicts the label for the given unlabeled dataset
    #Returns a list of predictions
    #-----------------------------------------------------#
    def classify(self, dataset):

        predictions = []
        with open(dataset, 'r') as f:
            for line in f:

                line = line.strip().split()
                #Store the probability for this line for each label
                LINE_PROBABILITY = [0.0] * self.label_count
                for i in range(self.label_count):
                    #Calculate thr probabilty
                    LINE_PROBABILITY[i] = math.log(self.label_data[i]) + self.P(line, i)

                #Get the maximum of the calculated label probabilities
                MAX = LINE_PROBABILITY.index(max(LINE_PROBABILITY))
                #Append mapped label string to predictions
                for x in self.label_mapping:
                    if x[0] == MAX:
                        predictions.append(x[1])

        return predictions
