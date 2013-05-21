#!/usr/bin/env python
import sys
import json
line =[]
terms =[]
scores={}
def make_dict(file1):
    scores = {} # initialize an empty dictionary
    for line in file1:
        term, score  = line.split("\t")
        scores[term] = int(score)

    #print scores
    return scores




def lines(fp):
    len1 = (len(fp.readlines()))
    fp.close()
    return len1

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    len2 =  lines(tweet_file)
    tweet_file = open(sys.argv[2])
    scores=make_dict(sent_file)
    for i in range(len2):
        line12 = tweet_file.readline()
        if(json.loads(line12).has_key('text')):
            line.append(json.loads(line12)["text"].encode('utf-8'))
        else:
            line.append("a")
    
    for tweet in line:
        terms.append(tweet.split())
    
    #print terms
    for words in terms:
        for word in words:
            total =0
            if scores.has_key(word):
                total = total + float(scores[word])
            else:
                total = total + 0.0
        print total
        
    
    tweet_file.close()

if __name__ == '__main__':
    main()

