import csv
import sys
import copy



f = open(sys.argv[1], 'rt')
header = True;
try:
    reader = csv.reader(f)
    featuresList = list(reader)      #list of features 
    totalRows =  len(featuresList)   #number of Rows - Total
    totalAttr =  len(featuresList[0])-1 #number of Attributes
    table = []
    for i in range(totalAttr):
    	table.append('Attribute'+str(i))
    #print table
    for row in featuresList:
    	for i in range(totalAttr):
			#print row[i]
			if(i==1):
				if(table['Attribute1'][row[i]]):
					print "nonono"


finally:
    f.close()

# with open('car.data', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in spamreader:
# 		print ', '.join(row)

