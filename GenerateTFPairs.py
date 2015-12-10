import csv

def validGene(gene, fileName):
	myFile = csv.reader(open(fileName+'Master.csv', 'rb'))
	for row in myFile:
		if gene in row[0]:
			return True
	return False


def readCSVFile(fileName):
	myFile = csv.reader(open(fileName+'TFPairs.csv', 'rb'))
	tfNum = 0
	for row in myFile:
		tfNum+=1
	TFPairs = []
	for i in xrange(tfNum):
		TFPairs+=[[0]*2]
	myFile2 = csv.reader(open(fileName+'TFPairs.csv', 'rb'))
	geneCount = 0
	for row in myFile2:
		tfString = row[0]
		slashCount = 0
		tfPiece = ""
		for c in tfString:
			if (slashCount % 2 == 0 and c == '/'):
				slashCount += 1
				tfPiece += " "
			elif c == '/':
				slashCount += 1
			elif c == ' ':
				continue
			else:
				tfPiece += c

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
		print(geneVector)
		index = 0
		finalgeneString = ""
		for gene in geneVector:
			if 'sup' in gene or 'sub' in gene or 'SUP' in gene or 'SUB' in gene:
				geneVector.remove(gene)
			elif validGene(gene[:5], fileName):
				finalgeneString += gene[:5] + " "
			elif validGene(gene[:4], fileName):
				finalgeneString += gene[:4] + " "
			elif validGene(gene[:3], fileName):
				finalgeneString += gene[:3] + " "
			else:
				geneVector.remove(gene)
		
		if(len(geneVector) > 0):
			TFPairs[geneCount][0] = tfPiece
			TFPairs[geneCount][1] = finalgeneString

		geneCount += 1
	return TFPairs
			


		

def createTFPairsFile(fileName):
	TFPairs = readCSVFile(fileName)
	cFile = csv.writer(open(fileName+"NewTFPairs.csv", 'wb'))
	for i in xrange(len(TFPairs)):
		cFile.writerow(TFPairs[i])

