import csv

def readCSVFile(fileName):
	myFile = csv.reader(open(fileName, 'rb'))
	tfNum = 0
	for row in myFile:
		tfNum+=1
	TFPairs = []
	for i in xrange(tfNum):
		TFPairs+=[[0]*2]
	myFile2 = csv.reader(open(fileName, 'rb'))
	geneCount = 0
	for row in myFile2:
		tfString = row[0]
		finaltfString = ""
		lenTF = len(tfString)
		for c in tfString:
			if ord(c) > 47 and ord(c) < 57:
				finaltfString += c
			elif ord(c) > 64 and ord(c) < 91:
				finaltfString += c
			elif ord(c) > 96 and ord(c) < 123:
				finaltfString += c
			elif ord(c) == 32:
				finaltfString += c
		geneString = row[1]
		finalgeneString = ""
		lenGene = len(geneString)
		for c in geneString:
			if ord(c) > 47 and ord(c) < 57:
				finalgeneString += c
			elif ord(c) > 64 and ord(c) < 91:
				finalgeneString += c
			elif ord(c) > 96 and ord(c) < 123:
				finalgeneString += c
			elif ord(c) == 32:
				finalgeneString += c

		TFPairs[geneCount][0] = finaltfString
		TFPairs[geneCount][1] = finalgeneString
		geneCount+=1
	return TFPairs

def createTFPairsFile(fileName):
	TFPairs = readCSVFile(fileName)
	cFile = csv.writer(open(""+fileName+".csv", 'wb'))
	for i in xrange(len(TFPairs)):
		cFile.writerow(TFPairs[i])


