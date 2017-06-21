import glob

array =[]

array = glob.glob("/home/kazutoshi/c2tm/C2tm/deNovo_Models/c2tm_bbmodels/*.pdb")

#print array

import os, numpy, sys

from prody import *

from pylab import *

files = array

for file in files:
    with open(file, 'w') as current_file:
        getCoords()
#print current_file









#with open(array) as fin:
#	for i in fin:
#		print i 







#filenames = array
#filedata = {filename: open(filename, 'w') for filename in filenames}
#print filedata



#for file in filedata.values():
#    file.close()

