import csv

sideEffectFile = open('sideEffect.txt')
testFile = open('test.txt')
csvfile = csv.writer(open('sideEffect-freq-test.csv', 'wb'))
# it can rewrite
sideEffectWords = []
for line in sideEffectFile:
    sideEffectWords.append(line.strip('\n'))
    print sideEffectWords

for sentence in testFile:
    flag = False
    for sideEffectWord in sideEffectWords:
        if sideEffectWord in sentence:
            flag = True

    if flag == True:
        csvfile.writerow(["1"])
    else:
        csvfile.writerow(["0"])



