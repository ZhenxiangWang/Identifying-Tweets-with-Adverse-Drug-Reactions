README: this file

dev.txt: initial dev.txt
train.txt: initial train.txt
test.txt: initial test.txt

dev-neg.csv: add negative attribute into initial dev.arff then transfer into csv format
dev-pos.csv: add positive attribute into initial dev.arff then transfer into csv format
dev-SI.csv: add sentiment intensity attribute into initial dev.arff then transfer into csv format
dev-side.csv:add side effect terms attribute into initial dev.arff then transfer into csv format
dev-all.csv: add all new attributes into initial dev.arff and remove id, then transfer into csv format


NegWord.txt: Negtive Word dictionary http://www.enchantedlearning.com/wordlist/negativewords.shtml
PosiWord.txt:  Positive Word dictionary. Retrived from http://www.enchantedlearning.com/wordlist/positivewords.shtml

NegWord-freq-dev.py: Output the frequency of the negative word appeared in each sentence in dev.txt
NegWord-freq-test.py: Output the frequency of the negative word appeared in each sentence in test.txt
NegWord-freq-train.py: Output the frequency of the negative word appeared in each sentence in train.txt

nltk-dev.py: calculate the compound value of polarity scores of each sentence in dev.txt
nltk-test.py: calculate the compound value of polarity scores of each sentence in test.txt
nltk-train.py: calculate the compound value of polarity scores of each sentence in train.txt

PosiWord-freq-dev.py： Output the frequency of the positive word appeared in each sentence in dev.txt
PosiWord-freq-test.py： Output the frequency of the positive word appeared in each sentence in test.txt
PosiWord-freq-train.py： Output the frequency of the positive word appeared in each sentence in train.txt

sideEffect.txt: side effect words dictionary. retrived from http://msb.embopress.org/content/6/1/343.long#DC1

sideEffect-freq-dev.py: Output whether side effect terms appeared in each sentence(using 0,1) in dev.txt
sideEffect-freq-test.py: Output whether side effect terms appeared in each sentence(using 0,1) in test.txt
sideEffect-freq-train.py: Output whether side effect terms appeared in each sentence(using 0,1) in train.txt

test.arff: initial test.arff
test.csv: transfer test.arff into csv format

train.csv: transfer train.arff into csv format

test-all.arff: add all new attributes into initial test.arff and remove id

train-neg.csv: add negative attribute into initial train.arff then transfer into csv format
train-pos.csv: add positive attribute into initial train.arff then transfer into csv format
train-SI.csv: add sentiment intensity attribute into initial train.arff then transfer into csv format
train-side.csv: add side effect terms attribute into initial train.arff then transfer into csv format

train-all.arff:add all new attributes into initial train.arff and remove id

p2-output.txt: the test predictions using final classifier




