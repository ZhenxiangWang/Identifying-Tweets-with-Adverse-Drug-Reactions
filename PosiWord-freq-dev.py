import csv
PosiWordFile=open('PosiWord.txt')
devFile=open('dev.txt')
csvfile= csv.writer(open('PosiWord-freq-dev.csv','wb'))
# it can rewrite
posiWords=[]
for line in PosiWordFile:
    posiWords.append(line.strip('\n'))
    print posiWords

for sentence in devFile:
    words=sentence.split()
    frequency=0
    for word in words:
        if word in posiWords:
            frequency=frequency+1
    csvfile.writerow([frequency])


