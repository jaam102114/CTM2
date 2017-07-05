import sys
import collections

i = 0

with open(sys.argv[1]) as f:
	while i < 12:
		read_data = f.readline()
		letters = collections.Counter(read_data)
		i += 1
		print letters
	
