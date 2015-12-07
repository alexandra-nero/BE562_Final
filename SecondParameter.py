#here is where the code to properly identify the second parameter
#DISTANCE, will be found from probabilities based on training data
'''pseudocode
create gaussian based on the model data:
 

calculate probability:
for every tf:
	for every gene:
		=tf/gene pair take their line numbers and calculate distance
'''
START_COLUMN = 4 
STOP_COLUMN = 5	#up to whoever creates the csv

BIN_SIZE = 250
TF_POS = 0
GENE_POS = 0
REG_GENES_POS = 1

def readTrainingDistances(genomeLength, pairFileName, genesFileName):
	"returns a list of distances from all TFs to all the genes they regulate given the genome's length, and the names of both the TF/Promoter pair file and the all genes file"
	trainingDistances = []
	genesFile = open(genesFileName)
	pairFile = open(pairFileName,'rb')
	for tf in pairFile:				#looking through all TFs
		tfPos = None
		tfName = tf[TF_POS]
		for gene in genesFile:		#looking for TF in gene file
			if gene[GENE_POS] == tfName:
				tfPos = gene[START_COLUMN]
				if tfPos == None:
					print ("ERROR: cannot read in position of TF")
					break
		if tfPos != None:
			regGenes = tf[REG_GENES_POS]
			regGenesList = []
			regGenesList = regGenes.split()
			pairDistances = []
			for regGene in xrange len(regGenesList):	#looping through all genes regulated
				regGeneName = regGenesList[regGene]
				for gene in genesFile:					#looking for gene regulated by TF in gene file
					if gene[GENE_POS] == regGeneName:
						regGenePos=gene[START_COLUMN]
						distance = []
						distance.append(abs(regGenePos-tfPos))
						distance.append(abs(distance[]-(genomeLength-1))
						trainingDistances.append(min(distance))
	return trainingDistances

def binTrainingDistances(genomeLength, trainingDistances):
	"counts frequencies for distances in each bin given the length of the genome and the list of distances between the TFs and the promoters they regulate"
	numberOfBins = (genomeLength/250)+1
	bin = [numberOfBins]
	for i in xrange len(trainingDistances)
		correctBin = ((int(trainingDistances[i]-1)/250))

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


