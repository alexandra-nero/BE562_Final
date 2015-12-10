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

def readPosTrainingDistances(genomeLength, pairFileName, genesFileName):
	"returns a list of distances from all TFs to all the genes they regulate given the genome's length, and the names of both the TF/Promoter pair file and the all genes file"
	posTrainDist = []
	negTrainDist = []
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
			posPairDist = []
			for regGene in xrange len(regGenesList):	#looping through all genes regulated
				regGeneName = regGenesList[regGene]
				for gene in genesFile:					#looking for gene regulated by TF in gene file
					if gene[GENE_POS] == regGeneName:
						regGenePos=gene[START_COLUMN]
						posDist = []
						posDist.append(abs(regGenePos-tfPos))
						posDist.append(abs(posDist[]-(genomeLength-1))
						posTrainDist.append(min(posDist))

	return (posTrainDist, negTrainDist)


def binTrainingDistances(genomeLength, trainingDistances):
	"counts frequencies for distances in each bin given the length of the genome and the list of distances between the TFs and the promoters they regulate"
	numberOfBins = (genomeLength/250)+1
	binnedDistances = [numberOfBins]
	totalFreq==0
	for i in xrange len(trainingDistances)
		correctBin = ((int(trainingDistances[i]-1)/250))
		binnedDistances[correctBin]+=1
		totalFreq+=1
	normDist = [x/totalFreq for x in binnedDistances]
	return normDist

