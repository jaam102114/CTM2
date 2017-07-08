import numpy as np
from collections import Counter
import sys

fh = open(sys.argv[1]) 
lines = fh.read() 
fh.close()

split = lines.split('\n')
sequence = ''

i = 0
while i < len(split):
	sequence += ''.join(split[i+1:i+2]) + '\n'
	i += 2

splitingAgain = sequence.split('\n')
sortedList = splitingAgain.sort(key = lambda x:len(x))
listToBeConverted = ('\n'.join(splitingAgain))

print listToBeConverted


Data = listToBeConverted
Freq = Counter([len(words) for words in Data.split()])
Result = []
for Num in range(1, max(Freq)+1):
    if Num in Freq:
        Result.append(Freq[Num])
    else:
        Result.append(0)

#sys.exit()

endOfHelixLength = -8
for s in Result:
	endOfHelixLength += 1
	if endOfHelixLength>0:
		print 'Count of loop length',endOfHelixLength,':',s
