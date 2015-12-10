import csv

#here is where the code to properly identify the second parameter
#DISTANCE, will be found from probabilities based on training data
'''pseudocode
create gaussian based on the model data:
 

calculate probability:
for every tf:
	for every gene:
		=tf/gene pair take their line numbers and calculate distance
'''
GENEFILE_START_COLUMN = 4 	
GENEFILE_STOP_COLUMN = 5	#don't need this atm
GENEFILE_GENE_POS = 0
GENEFILE_TFVAL_POS = 1

TFFILE_TF_POS = 0
TFFILE_REG_GENES_POS = 1

BIN_SIZE = 250

def readPosTrainingDistances(genomeLength, pairFileName, genesFileName):
	"returns a list of distances from all TFs to all the genes they regulate given the genome's length, and the names of both the TF/Promoter pair file and the all genes file"
	print("Starting to read in Training Distances")
	posTrainDist = []
	genesFile = open(genesFileName)
	pairFile = open(pairFileName,'rb')
	for tf in pairFile:				#looking through all TFs
		tfPos = None
		tfName = tf[TFFILE_TF_POS]
		for gene in genesFile:		#looking for TF in gene file
			if gene[GENEFILE_GENE_POS] == tfName:
				tfPos = gene[GENEFILE_START_COLUMN]
				if tfPos == None:
					print ("ERROR: cannot read in position of TF")
					break
		if tfPos != None:
			regGenes = tf[TFFILE_REG_GENES_POS]
			regGenesList = []
			regGenesList = regGenes.split()
			posPairDist = []
			for regGene in xrange(len(regGenesList)):	#looping through all genes regulated
				regGeneName = regGenesList[regGene]
				for gene in genesFile:					#looking for gene regulated by TF in gene file
					if gene[GENEFILE_GENE_POS] == regGeneName:
						regGenePos=gene[GENEFILE_START_COLUMN]
						posDist = []
						posDist.append(abs(regGenePos-tfPos))
						posDist.append(abs(posDist[0]-genomeLength))
						posTrainDist.append(min(posDist))
	enzymeMatrix = []
	negTrainDist = []
	for gene in genesFile:
		if gene[1] == 'F':
			enzymeMatrix.append(gene)
	for outerEnzyme in xrange(len(enzymeMatrix)):
		outerPos = outerEnzyme[GENEFILE_GENE_POS]
		for innerEnzyme in range(outerEnzyme, len(enzymeMatrix)):
			negDist = []
			innerPos = innerEnzyme[GENEFILE_GENE_POS]
			negDist.append(abs(outerPos - innerPos))
			negDist.append(abs(negDist[0]-genomeLength))
			negTrainDist.append(min(negDist))
	print("Normalizing positive training distances")
	posNormTrainDist = normTrainingDistances(genomeLength, posTrainDist)
	print("Normalizing negative training distances")
	negNormTrainDist = normTrainingDistances(genomeLength, negTrainDist)
	return (posNormTrainDist, negNormTrainDist)


def normTrainingDistances(genomeLength, trainingDistances):
	"counts frequencies for distances in each bin given the length of the genome and the list of distances between the TFs and the promoters they regulate, then normalizes them into probabilities"
	numberOfBins = (genomeLength/250)+1
	binnedDistances = [numberOfBins]
	totalFreq=0
	for i in xrange(len(trainingDistances)):
		correctBin = ((int(trainingDistances[i]-1)/250))
		binnedDistances[correctBin]+=1
		totalFreq+=1
	normDist=[]
	if totalFreq!=0:
		normDist = [x/totalFreq for x in binnedDistances]
		print("Total frequency is: ", totalFreq)

	return normDist

def secondParamMain(genomeLength, rootFileName):
	"manages the running of all other functions in second Parameter File"
	genesFileName = str(rootFileName)+"Master.csv"
	pairFileName = str(rootFileName)+"TFPairs.csv"
	posNegTup = readPosTrainingDistances(genomeLength, pairFileName, genesFileName) 
	
	outputCSV(posNegTup[0], posNegTup[1], rootFileName)


def outputCSV(posNormTrainDist, negNormTrainDist, rootFileName):
	"creates a CSV file from the normalized data. requires the yes and no normalized probability lists"
	print("Starting to write to CSV!")
	secondParamCSV = csv.writer(open(""+rootFileName+"secondParam.csv", "wb"))
	titleRow = ["Position (250 bp)","P(pair)","P(not pair)"]
	secondParamCSV.writerow(titleRow)
	for x in xrange(len(posNormTrainDist)):
		row = []
		row.append(x)
		row.append(posNormTrainDist)
		row.append(negNormTrainDist)
		secondParamCSV.writerow(row)
secondParamMain(4639675, "Ecoli_MG1655")