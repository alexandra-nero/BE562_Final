
import csv

def readFile(fileName):

	myFile = csv.reader(open(fileName, 'rb'))
	
	#counting how large the file is
	tfNum = 0
	for row in myFile:
		tfNum+=1
	myFile.close()
	
	#creating the matrix
	TFPairs = []
	for i in xrange(tfNum):
		TFPairs+=[[0]*2]

	myFile2 = csv.reader(open(fileName, 'rb'))
	geneCount = 0
	for row in myFile2:
	#here splice the tf names (ex. flhE // flhA // flhB) into name1 name2 
		tfString = row[0]
		lenTF = len(tfString)
		for c in tfString:
			if ord(c) > 47 and ord(c) < 57:
                tfString += c
            elif ord(c) > 64 and ord(c) < 91:
                tfString += c
            elif ord(c) > 96 and ord(c) < 123:
                tfString += c
            elif ord(c) == 32:
            	tfString += c

    #here we splice the gene names:
    	geneString = row[1]
		lenTF = len(geneString)
		for c in geneString:
			if ord(c) > 47 and ord(c) < 57:
                geneString += c
            elif ord(c) > 64 and ord(c) < 91:
                geneString += c
            elif ord(c) > 96 and ord(c) < 123:
                geneString += c
            elif ord(c) == 32:
            	geneString += c
        TFPairs[geneCount][0] = tfString
        TFPairs[geneCount][1] = geneString
        geneCount += 1

    myFile2.close()
    return TFPairs

def createTFPairsFile(fileName):
	TFPairs = readFile(fileName)
	cFile = csv.writer(open(""+fileName+".csv", 'wb'))
	for i in xrange(len(TFPairs)):
		csv.writerow(TFPairs[i])
	cfile.close()

