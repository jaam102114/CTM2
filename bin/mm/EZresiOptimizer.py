# Marco Mravic DeGrado Nov 2016
# Input a list of residues and a pdb
# output the top 3 residues and their EZ score, given the Z position of the Calpha for each residue

# assume the Ez_potential.py is in the user's path
from Ez_potentialNORM import *		# This is a version where potential dE is normalized to -0.2
									# so only maxima of apolars are same, thus position indicates residue ranked highest
from prody import * 
import sys, os, numpy as np

pdb = parsePDB(sys.argv[1])

# read in residu numbers, find them in the pdb, and calculate AA w/ highest EZ score for each
with open( sys.argv[2] ) as fin:
	for i in fin:


		resi 	= pdb.select( 'ca resnum ' + i.rstrip() )
		z 		= np.fabs( resi.getCoords()[0][2] )
#		if np.fabs(z) > 17:
#			print i.rstrip(), 'not really in membrane, skipping residue to avoid poor prediciton\n'
#			continue

		print (i.rstrip(), z)
		# compute the EZ score for each
		scores = [ (round( compute_Ez(k,z), 4 ), k) for k in Ez_potential.keys() if compute_Ez(k,z) < 0 ]
		# convert each score to 

		
		print (sorted( scores )[:3], '\n')
