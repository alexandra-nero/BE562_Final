import FirstParameter
import SecondParameter
import ThirdParameter
import GenerateTFPairs
import MasterCSVCreator
import csv
import math

#define all file Names here:
fileName ='Ecoli_MG1655'
geneNumber = 4500
geneLength = 4639675


def splitData(fileName):
	myFile = csv.reader(open(fileName+'TFPairs.csv', 'rb'))
	testFile = csv.writer(open(fileName+'TestTFPairs.csv', 'wb'))
	trainFile = csv.writer(open(fileName+'TrainTFPairs.csv', 'wb'))
	count = 0
	for row in myFile:
		if count == 8 or count == 9:
			testFile.writerow(row)
			if count == 9:
				count = 0
		else:
			trainFile.writerow(row)
		count += 1


def calculateAccuracy(ProbMatrix):
	testFile = csv.writer(open(fileName+'TestTFPairs.csv', 'wb'))
	for pair in trainFile:
		regGene = pair[0]
		tfGene = pair[1]
		for row in ProbMatrix:
			for column in ProbMatrix:




#main function for entire program

def runNaiveBayes():
	finalProb = csv.reader(open(fileName+'FinalProb.csv', 'wb'))
	finalMatrix = [] 
	MasterCSVCreator.createCSV(fileName, geneNumber)
	masterTFFile = csv.reader(open(fileName+'Master.csv', 'rb'))
	GenerateTFPairs.createTFPairsFile(fileName)
	splitData(fileName)

	#generate files from parameters
	SecondParameter.secondParamMain(geneLength, fileName)
	secondParamFile = csv.reader(open(fileName+"secondParam.csv", 'rb'))

	pairCount = 0
	for tfGene in masterTFFile:
		if (tfGene[MasterCSVCreator.TF_COLUMN] == 'T' or tfGene[MasterCSVCreator.TF_COLUMN] == 'unknown'):
			startTF = tfGene[MasterCSVCreator.START_COLUMN]
			masterRegFile = csv.reader(open(fileName+'Master.csv', 'rb'))
			for regGene in masterRegFile:
				startReg = tf[MasterCSVCreator.START_COLUMN]
				difference = abs(startTF-startReg)
				wrapAround = abs(geneLength-difference)
				totalDistance = min(difference, wrapAround)
				currentBin = totalDistance/SecondParameter.BIN_SIZE

				#first here
				secondProbabilities = secondParamFile[currentBin]
				thirdProbabilities = ThirdParameter.ThirdParam(tfGene, regGene)

		NaiveBayes = (firstProbabilities[0]+secondProbabilities[0]+thirdProbabilities[0])/(firstProbabilities[1]+secondProbabilities[1]+thirdProbabilities[1])
		NaiveBayesProb = math.log(NaiveBayes)
		finalRow = [tfGene, regGene, NaiveBayesProb]
		finalMatrix[pairCount][0] = tfGene
		finalMatrix[pairCount][1] = regGene
		finalMatrix[pairCount][2] = NaiveBayesProb
		finalProb.writerow(finalRow)
		print (calculateAccuracy(finalMatrix))





main()	

