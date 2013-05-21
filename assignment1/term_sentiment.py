#!/usr/bin/env python
import sys
import json
line =[]
terms =[]
total =[]
scores={}
dict ={}
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
    for index, words in enumerate(terms):
        for word in words:
            total.append(0)
            if scores.has_key(word):
                total[index] = total[index] + float(scores[word])
            else:
                total[index] = total[index] + 0.0
        #print total[index]
        
    for ind , tt in enumerate(terms):
        for t in tt:
            print t , total[ind]
        
    """for i in dict:
        if (scores.has_key(i)):
            pass
        else:
            print i, dict[i]"""
    
    tweet_file.close()

if __name__ == '__main__':
    main()

