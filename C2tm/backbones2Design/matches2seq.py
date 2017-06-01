from prody import * 
from PDButil import UnNatAA
import sys, os, numpy as np

flattened_Fasta = []
seenThisSeq = []

# calc and print closest inter-helical C-alpha distance for each residue (one side only)
miniPDB = parsePDB( sys.argv[2], subset='ca')
dMat = buildDistMatrix( miniPDB.select('chain A'), miniPDB.select('chain B') )
for i, j  in enumerate( dMat, 1):
	print i, round( np.min(j), 2 )
	
for i in os.listdir( sys.argv[1] ):

	path = os.path.join( sys.argv[1], i )
	with open( path ) as fin:
		rmsd = float( fin.readline().split()[1] )
	if rmsd > .5: continue

	pdb, header 	= parsePDB( path, subset='ca' , header=True)
	
	seq 	= ''.join(  [UnNatAA[ resi.getResname() ] for resi in pdb[:12] ] )
	seq2 	= ''.join(  [UnNatAA[ resi.getResname() ] for resi in pdb[12:] ] )

	if seq not in flattened_Fasta:
		flattened_Fasta.append( seq )
	if seq2 not in flattened_Fasta:
		flattened_Fasta.append( seq2 )


print '> %s' % sys.argv[1] 
for i in flattened_Fasta:
	print i