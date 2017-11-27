from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
sid=SentimentIntensityAnalyzer()

source=open("test.txt",'r')
csvfile= csv.writer(open('si-test.csv','wb'))

tweets=[]
scores=[]
compounds=[]
data=[]
for line in source:
    token=line.split('\t',3)
    tweets.append(token[2])
for tweet in tweets:
    s=sid.polarity_scores(tweet)
    csvfile.writerow([s['compound']])
    print s['compound']
    scores.append(s)

for score in scores:
    compounds.append(score['compound'])



