# CSV FILE SHOULD LOOK LIKE:
#GENE NAME  TF  FUNCTION                    START    STOP    DIRECTION   PROMOTER
#"gene1"    T/F Repressor/Activator/Both     978     1001       F/R       

import csv
import GenerateTFPairs

INFO_LINES = 50
DIRECTION_COLUMN = 4
TF_COLUMN = 1
START_COLUMN = 2
STOP_COLUMN = 3
REPRESSOR_COLUMN = 5
ACTIVATOR_COLUMN = 6
NAME_COLUMN = 0


def separate(fileName, GENE_NUM):
    myFile = open(fileName, 'r')
    BigData = []
    for i in xrange(GENE_NUM+ 1):
        BigData += [[0]*(INFO_LINES)]
    currentGene = -1
    count = 0
    start = False
    for line in myFile:
        if '     gene            ' in line:
            start = True
            count = 0
            currentGene+=1
        if (start):
            BigData[currentGene][count] = line
            count+=1

    return BigData, currentGene

def findNames(CSVMatrix, BigData):
    geneNumber = 0
    for currentString in xrange(len(BigData)):
        totalNames = ""
        count1 = 0
        count2 = 0
        for currentLine in xrange(INFO_LINES):
            myString = BigData[currentString][currentLine]
            saveName1 = False
            saveName2 = False
            if myString != 0:
                if 'synonym' in myString:
                    count1+= 1
                    if (count1 < 2):
                        for c in myString:
                            if c == '"' and saveName1 == True:
                                saveName1 = False
                                totalNames += " "
                            elif saveName1:
                                if ord(c) > 47 and ord(c) < 57:
                                    totalNames += c
                                elif ord(c) > 64 and ord(c) < 91:
                                    totalNames += c
                                elif ord(c) > 96 and ord(c) < 123:
                                    totalNames += c
                                elif ord(c) == 32:
                                    totalNames += c
                            elif c == '"' and saveName1 == False:
                                saveName1 = True
                if 'gene=' in myString:
                    count2 +=1
                    if (count2 < 2):
                        for c in myString:
                            if c == '"' and saveName2 == True:
                              saveName2 = False
                              totalNames +=" "
                            elif saveName2:
                                totalNames += c
                            elif c == '"' and saveName2 == False:
                                saveName2 = True
        CSVMatrix[geneNumber][NAME_COLUMN] = totalNames
        geneNumber+=1

#finding and parsing lines with stop/start data in them
#example:     gene            70387..71265
def findStartandStop(CSVMatrix, BigData):
    geneNumber = 0
    for currentString in xrange(len(BigData)):
        totalStart = ""
        totalStop = ""
        myString = BigData[currentString][0]
        if myString != 0:
            if '     gene            ' in myString:
                saveStart = False
                saveStop = False
                dotTimes=0
                for c in myString:
                    if ord(c) > 47 and ord(c) < 58:
                        if dotTimes > 1:
                            saveStart = True
                            saveStop = False
                        else:
                            saveStart = False
                            saveStop = True
                        if saveStart:
                            totalStop += c
                        if saveStop:
                            totalStart += c

                    if c == "(":
                        saveStart = True
                        saveStop = False
                    if c == ".":
                        if dotTimes > 1:
                            saveStop = True
                            saveStart = False
                        else:
                            dotTimes+=1
        if len(totalStart) > 0 and len(totalStop) > 0:
            CSVMatrix[geneNumber][START_COLUMN] = int(totalStart)
            CSVMatrix[geneNumber][STOP_COLUMN] = int(totalStop)
        geneNumber+=1

#simple string search to find the description word for the characteristics of the gene
def isTF(CSVMatrix, BigData):
    geneNumber = 0
    for currentString in xrange(len(BigData)):
        check = True
        for currentLine in xrange(INFO_LINES):
            myString = BigData[currentString][currentLine]
            if myString != 0:
                if "transcription" in myString or "regulator" in myString or 'repressor' in myString or 'activator' in myString:
                    CSVMatrix[geneNumber][TF_COLUMN] = True
                    check = False
        if check:
            CSVMatrix[geneNumber][TF_COLUMN] =False
        geneNumber+=1

def isRepressor(CSVMatrix, BigData):
    geneNumber = 0
    for currentString in xrange(len(BigData)):
        check = True
        for currentLine in xrange(INFO_LINES):
            myString = BigData[currentString][currentLine]
            if myString != 0:
                if "repressor" in myString:
                    CSVMatrix[geneNumber][REPRESSOR_COLUMN] = True
                    check = False
        if check:
            CSVMatrix[geneNumber][REPRESSOR_COLUMN] =False
        geneNumber+=1

def isActivator(CSVMatrix, BigData):
    geneNumber = 0
    for currentString in xrange(len(BigData)):
        check = True
        for currentLine in xrange(INFO_LINES):
            myString = BigData[currentString][currentLine]
            if myString != 0:
                if "activator" in myString:
                    CSVMatrix[geneNumber][ACTIVATOR_COLUMN] = True
                    check = False
        if check:
            CSVMatrix[geneNumber][ACTIVATOR_COLUMN] =False
        geneNumber+=1

def findDirection(CSVMatrix, BigData):
    geneNumber = 0
    for currentString in xrange(len(BigData)):
        myString = BigData[currentString][0]
        check = True
        if myString != 0:
            if "complement" in myString:
                check = False
                CSVMatrix[geneNumber][DIRECTION_COLUMN] = True
        if check:
            CSVMatrix[geneNumber][DIRECTION_COLUMN] = False
        geneNumber+=1

def createCSV():

    fileName = raw_input('Enter the name of the GenBank file: ')
    geneNumber = raw_input('Enter the number of genes: ')
    fileName2 = raw_input('Enter the name of the TF/Gene pair file: ')
    GENE_NUM = int(geneNumber)

    cfile = csv.writer(open(""+fileName+".csv", "wb"))
    DNAMatrix, currentGene = separate(fileName, GENE_NUM)
    CSVMatrix = []
    for i in xrange(GENE_NUM+1):
        CSVMatrix += [[0]*(ACTIVATOR_COLUMN+1)]
    print('Taking Information from file...')
    findDirection(CSVMatrix, DNAMatrix)
    isActivator(CSVMatrix, DNAMatrix)
    isRepressor(CSVMatrix, DNAMatrix)
    isTF(CSVMatrix, DNAMatrix)
    findStartandStop(CSVMatrix, DNAMatrix)
    findNames(CSVMatrix,DNAMatrix)
    characteristicsVector = []
    GENE_NUM = currentGene
    print('Creating .csv file of characteristics...')
    for geneNumber in xrange(GENE_NUM+1):
        characteristicsVector.append(CSVMatrix[geneNumber][0])
        if CSVMatrix[geneNumber][TF_COLUMN]:
            characteristicsVector.append('T')
            if CSVMatrix[geneNumber][REPRESSOR_COLUMN] and CSVMatrix[geneNumber][ACTIVATOR_COLUMN]:
                characteristicsVector.append('Both')        
            elif CSVMatrix[geneNumber][REPRESSOR_COLUMN]:
                characteristicsVector.append('Repressor')
            elif CSVMatrix[geneNumber][ACTIVATOR_COLUMN]:
                characteristicsVector.append('Activator')
            else:
                characteristicsVector.append('unknown')
        else:
            characteristicsVector.append('F')
            characteristicsVector.append('N/A')

        if CSVMatrix[geneNumber][START_COLUMN]:
            characteristicsVector.append(CSVMatrix[geneNumber][STOP_COLUMN])
            characteristicsVector.append(CSVMatrix[geneNumber][START_COLUMN])
        else:
            characteristicsVector.append(CSVMatrix[geneNumber][START_COLUMN])
            characteristicsVector.append(CSVMatrix[geneNumber][STOP_COLUMN])

        if CSVMatrix[geneNumber][DIRECTION_COLUMN] == False:
            characteristicsVector.append('F')
        else:
            characteristicsVector.append('R')
        cfile.writerow(characteristicsVector)
        del characteristicsVector[:]
    
    print('Creating csv file of the TF/Gene Pairs...')
    #creating the accompanying tf/gene pair file name
    GenerateTFPairs.createTFPairsFile(fileName2)

createCSV()