#!/usr/bin/python
# example of program that calculates the total number of times each word has been tweeted.
# written by Gene Der Su for Insight coding challenge.

import sys
import math


## read data file
inputFile=sys.argv[1]
with open(inputFile,'r') as i:
    lines = i.readlines()

maxLetter=0
maxCount=1
wordCount={}
for line in lines:
    ## count number of times each word appears while keeping the number of maximum letter and maximum count
    words = line.split()
    for word in words:
        if maxLetter<len(word):
            maxLetter=len(word)
        if word in wordCount:
            wordCount[word]=wordCount[word]+1
            if maxCount<wordCount[word]:
                maxCount=wordCount[word]
        else:
            wordCount[word]=1

## calculate the digits needed for the number of count
maxCountDigit=int(math.ceil((math.log10(maxCount))))

## write the result into the output file
outputFile=sys.argv[2]
with open(outputFile,'w') as o:
    for word in sorted(wordCount):
        resultingString = '{0:%s}      {1:%sd}'%(maxLetter,maxCountDigit)
        o.write(resultingString.format(word, wordCount[word]))
        o.write('\n')

        
