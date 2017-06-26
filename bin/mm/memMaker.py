from prody import *
import sys
from PDButil import random_membrane_res, UnNatAA
from random import randint

def random_membrane_res(exclude=[]):
	probs = ['A', 'F', 'V', 'I', 'L', 'L', 'L', 'L', 'L', 'L']
	for i in exclude:
		probs.remove(i)
	newLength = len(probs)
	print probs
	return probs[randint( 0 , newLength - 1) ]

# use a few rule-based moves to randomly pick LVIFA for an amino acid sequence... 
# Rule 1: re-pick if two beta-branched in a row IVT
# Rule 2: re-pick if small residue selected but small exists at (AGST) at i+4 or i+7 
# Go N to C so each pick dependent on input sequence and previous picks
# Cys in existing sequence denoted residue to randomize
# python ~/bin/memMaker.py aligned_a3d_2redesignEZout.pdb > a3d_memMade.txt

inPDB = parsePDB( sys.argv[1], subset='ca' )

for atom in inPDB:

	# select a residue at each cys, and initialize the list of residues to exclude from random calculation
	if atom.getResname() != 'CYS':
		print UnNatAA[ atom.getResname() ], 
		continue
	exclude = []
		
	## Rule 1: repick if new amino acid picked would make succeessive beta branched residue

	# get residue index of current CA in pdb atom array,  1 - resnum
	curResNum = atom.getResnum() - 1
	prvResNum = curResNum - 1 
	nxtResNum = curResNum + 1

	# i plus and minus 4 and 7 check for small amino acids
	im4Resnum = curResNum - 4 
	ip4Resnum = curResNum + 4 
	im7Resnum = curResNum - 7 
	ip7Resnum = curResNum + 7 

	if prvResNum >= 0 : 
		prvRes = UnNatAA[ inPDB[prvResNum].getResname() ] 
		if prvRes in ['I', 'V', 'T'] :
			exclude.extend( ['I', 'V'] )

	if nxtResNum < len( inPDB ):
		nxtRes = UnNatAA[ inPDB[nxtResNum].getResname() ] 		# convert 3-letter code to 1 letter code
		if nxtRes in ['I', 'V', 'T'] and 'I' not in exclude:
			exclude.extend( ['I', 'V'] )

	if im4Resnum >= 0 :
		im4Res =  UnNatAA[ inPDB[im4Resnum].getResname() ] 
		if im4Resnum in ['A', 'G', 'S']:
			exclude.append('A')

	if ip4Resnum < len( inPDB ) :
		ip4Res =  UnNatAA[ inPDB[ip4Resnum].getResname() ] 
		if ip4Resnum in ['A', 'G', 'S'] and 'A' not in exclude:
			exclude.append('A')

	if ip7Resnum < len( inPDB ) :
		ip7Res =  UnNatAA[ inPDB[ip7Resnum].getResname() ] 
		if ip7Resnum in ['A', 'G', 'S'] and 'A' not in exclude:
			exclude.append('A')
			print 'prevented A'

	if im7Resnum >= 0 :
		im7Res =  UnNatAA[ inPDB[im7Resnum].getResname() ] 
		if im7Resnum in ['A', 'G', 'S']and 'A' not in exclude:
			exclude.append('A')

	newRes = random_membrane_res(exclude)
	print newRes, 



	# Now Rule #2			





#	print newRes, atom.getResnum()

	#sys.exit()
