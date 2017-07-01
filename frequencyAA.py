import sys
import collections
stripping = []
stripping2 = []
elements =[]
record = []
counting = 12
placeholding = 0


while True:
	with open(sys.argv[1]) as f:	
		for line in f:			
			stripping+= line.strip()
			stripping2 += line.strip() + '\n'
			dataset_list = ''.join(stripping2)			
			elements += stripping[-12+counting+placeholding]
			counting+= 12
			if counting >131:
				placeholding+=1
				record.append(elements)
				print record
				stripping = []
				stripping2 = []
				elements =[]
				record = []
				counting = 12			
	if placeholding > 11:
		break

counter =0
for i in dataset_list:
	print 


sys.exit()

for s in dataset_list:
	letters = collections.Counter(record)
	print s,letters
























#sys.exit()
#dataset_list = ''.join(stripping)
#print dataset_list
#print firstElements
