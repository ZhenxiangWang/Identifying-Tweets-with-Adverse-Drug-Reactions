import csv
NegWordFile=open('NegWord.txt')
trainFile=open('train.txt')
csvfile= csv.writer(open('NegWord-freq-train.csv','wb'))
# it can rewrite
negWords=[]
for line in NegWordFile:
    negWords=line.split('\r')
    print negWords

for sentence in trainFile:
    words=sentence.split()
    frequency=0
    for word in words:
        if word in negWords:
            frequency=frequency+1
    csvfile.writerow([frequency])


