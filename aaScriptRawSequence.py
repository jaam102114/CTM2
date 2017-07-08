import sys

def replace_all(text,dic):
	for i,j in dic.iteritems():
		text = text.replace(i,j)
	return text

stripping =[]

default = ''
aa =  {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', '[' : '', ']': '',
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M', "'" :'', " " :'', 'MSE': 'M'}

simpleText = '' 

with open(sys.argv[1]) as f:	
	for line in f:	
		stripping= line.strip() + ' '
		if len(stripping)<20:
			simpleText+= ''.join(stripping[0:len(line)])+ '\n'
		else:
			simpleText+= ''.join(stripping[0:len(line)])

txt = replace_all(simpleText, aa)

print txt

