import sys, os, numpy 
from prody import *



# enter into script:
# python directoryScriptForMoleculeDistance.py /home/kazutoshi/c2tm/C2tm/deNovo_Models/master_searches/matches_1_params.txt /home/kazutoshi/c2tm/C2tm/deNovo_Models/c2tm_bbmodels


print '\n'

placeholder = []
text=''

counter = 0
with open(sys.argv[1]) as f:	
	for line in f:
		line2 = line.split()		
		if "Ro" in line:
			continue
		if int(line[0:3]) < 250:
			continue
		else:
			basename = os.path.basename(line2[1])		
			full_filepath = os.path.join(sys.argv[2], basename )			
			test = parsePDB(full_filepath)		
			chainA = test.select('chain A ca')
			chainB = test.select('chain B ca')
			distanceMatrix = buildDistMatrix(chainA,chainB)
			minValues = distanceMatrix.min()
			text+= line.rstrip() + ' ' + str( minValues ) + '\n'
			
print text


 
			
			
#with open(sys.argv[1],'a') as f:
#	f.write(str(minValues))