#here is where the code to properly identify the first parameter
#COREGULATION, direct relationship between coregultion and possibility of TF promoter pair

def normTrainingDistances(normCoreg):
	#"counts frequencies for distances in each bin given the length of the genome and the list of distances between the TFs and the promoters they regulate, then normalizes them into probabilities"
	numberOfBins = 20	#.05 per bin
	binnedCoreg[numberOfBins]
	for k in xrange(numberOfBins):	#initializing binnedCoreg as int vals
		binnedCoreg+=[0]	
	totalFreq=0
	for i in xrange(len(normCoreg)):	#going through all values
		correctBin = (int(normCoreg*20))
		binnedCoreg[correctBin]+=1
		totalFreq +=1
	
	normDist=[]
	if totalFreq!=0:
		normDist = [x/totalFreq for x in binnedCoreg]
		print("Total frequency is: ", totalFreq)

return normCoreg