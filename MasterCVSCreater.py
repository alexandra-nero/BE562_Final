import csv

infoLines = 200

def separate(fileName, geneNum):
    myFile = open(fileName, 'r')
    BigData = []
    for i in xrange(geneNum + 1):
        BigData += [[0]*(infoLines)]
    currentGene = 0
    count = 0
    for line in myFile:
        #print(line)
        if '     gene            ' in line:
            currentGene+=1
            count = 0

        BigData[currentGene][count] = line
        count+=1

    return BigData, currentGene


def findNames(CVSMatrix, BigData, currentGene):
    for currentString in xrange(currentGene):
        totalNames = ""
        for currentLine in xrange(infoLines):
            myString = BigData[currentString][currentLine]
            if 'synonym' in myString:
                saveName = False
                for c in myString:
                    if ord(c) == 34 and saveName == False:
                        saveName = True
                    if ord(c) == 34 and saveName == True:
                        pass
            if 'gene=' in myString:
                saveName = False
                for c in myString:
                    if ord(c) == 34:




#finding and parsing lines with stop/start data in them
#example:     gene            70387..71265
def findStartandStop(CVSMatrix, BigData, currentGene):
    geneNumber = 0
    for currentString in xrange(currentGene):
        totalStart = ""
        totalStop = ""
        for currentLine in xrange(infoLines):
            myString = BigData[currentString][currentLine]
            if '     gene            ' in myString:
                saveStart = False
                saveStop = False
                for c in myString:
                    if ord(c) > 47 and ord(c) < 58:
                        saveStart = True
                        saveStop = False

                    if saveStart:
                        totalStart += c
                    if saveStop:
                        totalStop += c

                    if c == "(":
                        saveStart = True
                        saveStop = False
                    if c == "."
                        if dotTimes > 1:
                            saveStop = True
                            saveStart = False
        CVS[geneNumber][START_COLUMN] = totalStart
        CVS[geneNumber][STOP_COLUMN] = totalStop
        geneNumber+=1


#simple string search to find the description word for the characteristics of the gene
def isTF(BigData, geneName):
    geneNumber = 0
    for currentString in xrange(currentGene):
        for currentLine in xrange(infoLines):
            myString = BigData[currentString][currentLine]
            if "transcription" in myString or "regulator" in myString:
                CVSMatrix[geneNumber][DIRECTION_COLUMN] = True
        CVSMatrix[geneNumber][TF_COLUMN] =False
        geneNumber+=1

def isRepressor(CVSMatrix, BigData, currentGene):
    geneNumber = 0
    for currentString in xrange(currentGene):
        for currentLine in xrange(infoLines):
            myString = BigData[currentString][currentLine]
            if "repressor" in myString:
                CVSMatrix[geneNumber][DIRECTION_COLUMN] = True
        CVSMatrix[geneNumber][REPRESSOR_COLUMN] =False
        geneNumber+=1

def isActivator(CVSMatrix, BigData, currentGene):
    geneNumber = 0
    for currentString in xrange(currentGene):
        for currentLine in xrange(infoLines):
            myString = BigData[currentString][currentLine]
            if "activator" in myString:
                CVSMatrix[geneNumber][DIRECTION_COLUMN] = True
        CVSMatrix[geneNumber][ACTIVATOR_COLUMN] =False
        geneNumber+=1

def findDirection(CVSMatrix, BigData, currentGene):
    geneNumber = 0
    for currentString in xrange(currentGene):
        for currentLine in xrange(infoLines):
            myString = BigData[currentString][currentLine]
            if "complement" in myString:
                CVSMatrix[geneNumber][DIRECTION_COLUMN] = True
        CVSMatrix[geneNumber][DIRECTION_COLUMN] =False
        geneNumber+=1



def main():

    cfile = csv.writer(open("myFile.csv", "wb"))
    DNAMatrix, currentGene = separate("Ecoli_MG1655.gb.txt", 4500)
    CSVMatrix = []
    for i in xrange(9):
        CVSMatrix += [[0]*currentGene]



