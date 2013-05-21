#!/usr/bin/env python
import sys
import json
line =[]
terms =[]
dict1={}




def lines(fp):
    len1 = (len(fp.readlines()))
    fp.close()
    return len1

def main():
    tweet_file = open(sys.argv[1])
    len2 =  lines(tweet_file)
    tweet_file = open(sys.argv[1])
    
    for i in range(len2):
        line12 = tweet_file.readline()
        if(json.loads(line12).has_key('text')):
            line.append(json.loads(line12)["text"].encode('utf-8'))
        else:
            line.append(" ")
    
    for tweet in line:
        terms.append(tweet.split())
    
    #print terms
    total_words =float(0)
    for words in terms:
        total_words= float(total_words + len(words))
        
    #print total_words
    
    
    for tt in terms:
        for t in tt:
            if(dict1.has_key(t)):
                dict1[t] = float(dict1[t]+1.0)
            else:
                dict1[t]= 1.0
                
    
    for i in dict1:
        print i , dict1[i]/total_words
    
        
    
    tweet_file.close()

if __name__ == '__main__':
    main()

