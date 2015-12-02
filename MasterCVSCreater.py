import csv


def separate(fileName, geneNum):
    myFile = open(fileName, 'r')
    BigData = []
    currentGene = 0
    for i in xrange(geneNum + 1):
        BigData += [[0]*(30-1)]

    while (fileName.readline()):
        if "     gene" in fileName.readline():
            currentGene++
        BigData[currentGene][i] = fileName.readline()
        i+=1

    print("hi")
    print(BigData)




print("hi")
cfile = csv.writer(open("myFile.csv", "wb"))
separate("Ecoli_MG1655.gb.txt", 4381)



