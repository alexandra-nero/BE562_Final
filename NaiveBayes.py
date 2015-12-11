#import FirstParameter
#import SecondParameter
#import ThirdParameter
import GenerateTFPairs
import MasterCSVCreator
import csv

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


#def calculateAccuracy():



#main function for entire program

def main():
	MasterCSVCreator.createCSV(fileName, geneNumber)
	GenerateTFPairs.createTFPairsFile(fileName)
	splitData(fileName)

main()	

