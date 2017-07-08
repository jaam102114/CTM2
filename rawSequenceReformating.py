import sys
import collections

# script used to convert a list of simiar sized amino acids sequence frequecny in 1 letter code format:
#		ENSURE THE FILE HAS NO BLK SPACE AT THE END

with open(sys.argv[1]) as input_file:
    rows = input_file.readlines()
rows = zip(*[row.strip() for row in rows])
rows = [''.join(row) for row in rows]


string = ''
counter = 0
for i in rows:
	string += i
	letters = collections.Counter(string)
	counter += 1	
	print 'Residue',counter, 'has the frequency below'	
	print letters
	print '\n'



# prints the reformatted sequences to apply a letter frequency script
	
#print string