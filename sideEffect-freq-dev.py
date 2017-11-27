import csv
sideEffectFile=open('sideEffect.txt')
devFile=open('dev.txt')
csvfile= csv.writer(open('sideEffect-freq-dev.csv','wb'))
# it can rewrite
sideEffectWords=[]
for line in sideEffectFile:
    sideEffectWords.append(line.strip('\n'))
    print sideEffectWords

for sentence in devFile:
    flag=False
    for sideEffectWord in sideEffectWords:
        if sideEffectWord in sentence:
            flag=True
            
    if flag==True:
        csvfile.writerow(["1"])
    else:
        csvfile.writerow(["0"])



