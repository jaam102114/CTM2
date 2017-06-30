import sys
stripping = []
elements =[]
record = []
counting = 12
placeholding = 0


while True:
	with open(sys.argv[1]) as f:	
		for line in f:			
			stripping+= line.strip()
			stripping2 += line,strip() + '\n'
			elements += stripping[-12+counting+placeholding]
			counting+= 12
			print elements
			if counting >131:
				placeholding+=1
				record.append(elements)
				print record
				stripping = []
				elements =[]
				record = []
				counting = 12
				dataset_list = ''.join(stripping2)
				print dataset_list
	if placeholding > 11:
		break
#sdsd























#sys.exit()
#dataset_list = ''.join(stripping)
#print dataset_list
#print firstElements
