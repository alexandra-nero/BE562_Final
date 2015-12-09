import FirstParameter
import SecondParameter
import ThirdParameter
import MasterCSVCreator

#define all file Names here:
fileNames =['Ecoli_MG1655']
geneNumber = ['4500']



#main function for entire program

def main():
	geneCount = 0
	for geneFile in fileNames:
		MasterCSVCreator.createCSV(geneFile, geneNumber[geneCount])
		geneCount+=1
main()	