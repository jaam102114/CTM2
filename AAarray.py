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
			dataset_list2 = ''.join(stripping)			
			elements += stripping[-12+counting+placeholding]
			counting+= 12
			if counting >636:
				placeholding+=1
				record.append(elements)
				#print record
				print elements
				final_array = elements
				stripping = []
				stripping2 = []
				elements =[]
				record = []
				counting = 12			
	if placeholding > 53:
		break


sys.exit()

for s in dataset_list:
	letters = collections.Counter(record)
	print s,letters



