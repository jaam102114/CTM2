import sys

def replace_all(text,dic):
	for i,j in dic.iteritems():
		text = text.replace(i,j)
	return text

stripping =[]

default = ''
aa =  {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M', ' ':''}

simpleText = ''

counter = 104

with open(sys.argv[1]) as f:	
	for line in f:	
		stripping+= line.strip() + ' '
		simpleText+= '>' + ''.join(stripping[-104+counter:-97+counter]) + '\n' 	+ ''.join(stripping[-96+counter:-49+counter]) + '\n'
		counter = counter + 104
			
txt = replace_all(simpleText, aa)

print txt

