#here is where the code to properly identify the second parameter
#DISTANCE, will be found from probabilities based on training data
'''pseudocode
create gaussian based on the model data:
 

calculate probability:
for every tf:
	for every gene:
		=tf/gene pair take their line numbers and calculate distance
'''
START_COLUMN = start 
STOP_COLUMN = STOP_COLUMN	#up to whoever creates the csv
BIN_SIZE = 250

def SecondParam():

return

def readCSV(lineNum, csvFile):	#taking in CSV data
csvFile = open(csvFile)
temp = []
geneCount = 0
for line in csvFile:
	temp.append(line)
	if lineNum == geneCount:
		start = temp[geneCount][START_COLUMN]
		stop = temp[geneCount][STOP_COLUMN]
		return start, stop
	geneCount+=1

return

def binData():	#putting data into bins by distance -- should use binSize = 250

def gaussianize(): #makes binned data Gaussian -- should use gaussian library?
return


