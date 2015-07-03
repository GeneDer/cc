#!/usr/bin/python
# example of program that calculates the median number of unique words per tweet.
# written by Gene Der Su for Insight coding challenge.

import sys
import math


inputFile=sys.argv[1]
with open(inputFile,'r') as i:
    lines = i.readlines()


uniqueWordCountArray=[]
for line in lines:
    words = line.split()
    uniqueWordCountArray.append(len(list(set(words)))) 
##    for word in words:
##        if maxLetter<len(word):
##            maxLetter=len(word)
##        if word in wordCount:
##            wordCount[word]=wordCount[word]+1
##            if maxNumber<wordCount[word]:
##                maxNumber=wordCount[word]
##        else:
##            wordCount[word]=1
##maxNumberDigit=int(math.ceil((math.log10(maxNumber))))
##
##outputFile=sys.argv[2]
##with open(outputFile,'w') as o:
##    for word in sorted(wordCount):
##        resultingString = '{0:%s}      {1:%sd}'%(maxLetter,maxNumberDigit)
##        o.write(resultingString.format(word, wordCount[word]))
##        o.write('\n')

print uniqueWordCountArray
