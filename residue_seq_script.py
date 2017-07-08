import os

from prody import *

import sys

for i in os.listdir('.'):
	if i.endswith(".pdb"):
		pdb=parsePDB(i, subset='ca')
		print pdb.getResnames()



sys.exit()

