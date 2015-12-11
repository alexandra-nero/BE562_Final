import csv

def validGene(gene, fileName):
	myFile = csv.reader(open(fileName+'Master.csv', 'rb'))
	for row in myFile:
		if gene in row[0]:
			return True
	return False


def readCSVFile(fileName):
	myFile = csv.reader(open(fileName+'OldTFPairs.csv', 'rb'))
	tfNum = 0
	for row in myFile:
		tfNum+=1
	TFPairs = []
	for i in xrange(tfNum*5):
		TFPairs+=[[0]*2]
	myFile2 = csv.reader(open(fileName+'OldTFPairs.csv', 'rb'))
	geneCount = 0
	for row in myFile2:
		tfString = row[0]
		slashCount = 0
		tfPiece = ""
		tfPieces = []
		index = 0
		for c in tfString:
			if (slashCount % 2 == 0 and c == '/'):
				if (tfString[index+1] == '/'):
					slashCount += 1
					if (validGene(tfPiece, fileName)):
						tfPieces.append(tfPiece)
					tfPiece = ""
			elif c == '/':
				slashCount += 1
			else:
				tfPiece += c
			index+=1

		geneString = row[1]
		slashCount = 0
		genePiece = ""
		geneVector = []
		for c in geneString:
			if (slashCount % 2 == 0 and c == '/'):
				slashCount += 1
				geneVector.append(genePiece)
				genePiece = ""
			elif c == '/':
				slashCount += 1
			elif c == ' ':
				continue
			else:
				genePiece += c
		geneVector.append(genePiece)
		index = 0
		finalgeneString = ""
		newGeneVector = []
		for gene in geneVector:
			geneLower = gene[0].lower() + gene[1:]
			if 'sup' in gene or 'sub' in gene or 'SUP' in gene or 'SUB' in gene:
				continue
			elif validGene(gene[:5]+ " ", fileName) or validGene(geneLower[:5]+ " ", fileName):
				newGeneVector.append(geneLower[:5])
			elif validGene(gene[:4] + " ", fileName) or validGene(geneLower[:4] + " ", fileName):
				newGeneVector.append(geneLower[:4])
			elif validGene(gene[:3] + " ", fileName) or validGene(geneLower[:3] + " ", fileName):
				newGeneVector.append(geneLower[:3])
			else:
				continue

		newNewGeneVector = []
		for i in newGeneVector:
			if i not in newNewGeneVector:
				newNewGeneVector.append(i)

		if(len(newNewGeneVector) > 0 and len(tfPieces) > 0):
			for tfthing in tfPieces:
				for genething in newNewGeneVector:
					TFPairs[geneCount][0]= tfthing.strip()
					TFPairs[geneCount][1] = genething.strip()
					geneCount += 1
	return TFPairs
			
def createTFPairsFile(fileName):
	print('Creating .csv file of the TF/Gene Pairs...')
    #creating the accompanying tf/gene pair file name
	TFPairs = readCSVFile(fileName)
	cFile = csv.writer(open(fileName+"TFPairs.csv", 'wb'))
	for i in xrange(len(TFPairs)):
		if TFPairs[i][0] != 0 and TFPairs[i][1] != 0:
			cFile.writerow(TFPairs[i])

