# naive-bayes-classifier
Generic Naive Bayes classifier buit in python

# Usage
First train the classifier
<code>python nblearn.py [training_file] [model_file_name]</code>

Then run the classifier on a test set
<code>python nbclassify.py [model_file] [testing_file]</code>


The NB.py class is standalone and can be used as is by importing it into your project.
Use the functions from the class as shown in the nbtrain.py and nbclassify.py example files.


# Notes on the data
The training and testing file data should be in the following format<br/>
<code>LABEL FEATURE1:FREQ FEATURE2:FREQ FEATURE3:FREQ ... </code><br>
<code>LABEL FEATURE1:FREQ FEATURE3:FREQ FEATURE20:FREQ ... </code>

LABEL can be a string as "POSITIVE" or "SPAM" <br>
FEATURES are numeric starting from 1<br>
FREQ is the numeric value of the number of time the corrosponding feature occours in the sample<br>

Example: The positive sample "Hello world . The world is beautiful ." is written as <br>
<code>POSITIVE 1:1 2:2 3:2 4:1 5:1 6:1</code><br><br>
where:
<ul>
<li> 1 = "Hello" </li>
<li> 2 = "world" </li>
<li> 3 = "." </li>
<li> 4 = "The" </li>
<li> 5 = "is" </li>
<li> 6 = "beautiful" </li>
</ul>


