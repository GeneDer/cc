#!/usr/bin/python
# example of program that calculates the median number of unique words per tweet.
# written by Gene Der Su for Insight coding challenge.

import sys
import math


inputFile=sys.argv[1]
with open(inputFile,'r') as i:
    lines = i.readlines()


uniqueWordCountArray=[]
medianArray=[]
medianIndex=0
for line in lines:
    words = line.split()
    uniqueWordCount=len(list(set(words)))
    uniqueWordCountArray.append(uniqueWordCount)
    for index, wordCount in enumerate(uniqueWordCountArray):
        if wordCount>uniqueWordCount:
            uniqueWordCountArray.insert(index,uniqueWordCount)
            uniqueWordCount.pop(len(uniqueWordCount)-1)
    
    if len(uniqueWordCountArray)%2==0:
        median=0.5*(uniqueWordCountArray[medianIndex]+uniqueWordCountArray[medianIndex+1])
    elif len(uniqueWordCountArray)!=1:
        medianIndex=medianIndex+1
        median=uniqueWordCountArray[medianIndex]
    else:
        median=uniqueWordCount
    medianArray.append(median)
        
outputFile=sys.argv[2]
with open(outputFile,'w') as o:
    for median in sorted(medianArray):
        o.write(str(median))
        o.write('\n')
