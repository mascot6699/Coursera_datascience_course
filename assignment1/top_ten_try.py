#!/usr/bin/env python
import sys
import json
line =[]
terms =[]
country=[]
total=[]
scores={}
dict1={}





def lines(fp):
    len1 = (len(fp.readlines()))
    fp.close()
    return len1

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    len2 =  lines(tweet_file)
    tweet_file = open(sys.argv[1])
    for i in range(len2):
        line12 = tweet_file.readline()
        if(json.loads(line12).has_key('text')):
            line.append(json.loads(line12)["text"].encode('utf-8'))
        else:
            line.append("a")
    
    for tweet in line:
        terms.append(tweet.split())
    
    for index, words in enumerate(terms):
        for word in words:
            if (word[:1]=="#"):
                if dict1.has_key(word[1:]):
                    dict1[word[1:]]= dict1[word[1:]] + 1.0
                else:
                    dict1[word[1:]]=1.0
                     
    
    for i in range(9):    
        str12 =  sorted(dict1.iteritems(), key=lambda item: -item[1])[i]
        print str12[0],str12[1]
    
    
    tweet_file.close()

if __name__ == '__main__':
    main()

