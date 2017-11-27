import csv
PosiWordFile=open('PosiWord.txt')
trainFile=open('train.txt')
csvfile= csv.writer(open('PosiWord-freq-train.csv','wb'))
# it can rewrite
posiWords=[]
for line in PosiWordFile:
    posiWords.append(line.strip('\n'))
    print posiWords

for sentence in trainFile:
    words=sentence.split()
    frequency=0
    for word in words:
        if word in posiWords:
            frequency=frequency+1
    csvfile.writerow([frequency])


