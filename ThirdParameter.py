#here is where the code to properly identify the third parameter
#COMMON MOTIFS now uses sequence alignment to find the probability based on the motif

import sys, csv, random
import pfinder3 as pf

mastercsvfile = 'Ecoli_MG1655Master.csv'
thirdparamcsv = 'Ecoli_MG1655thirdParam.csv'
fastafile = 'sequence.fasta'
PROM_LENGTH = 200
BIN_SIZE = 1
THRESHOLD = 4
MATCH = 1
MISMATCH = -1

def findSeq(pos,gfile):
    start = pos[0]-1
    stop = pos[1]
    genome = ''

    with open(gfile, "r") as f:
        for line in f:
            if line.startswith('>'):
                pass
            else:
                line = line.strip()
                genome += line

    if start < 0:
        start = len(genome) + start
        sequence = genome[start:len(genome)] + genome[0:stop]
    elif stop > len(genome)-1:
        stop = stop - len(genome)
        sequence = genome[start:len(genome)] + genome[0:stop]
    else:
        sequence = genome[start:stop]

    return sequence

def reVerse(sequence):
    complement = [0] * len(sequence)

    for i in range(len(sequence)):
        if sequence[i] == 'A':
            complement[len(sequence)-i-1] = 'T'
        elif sequence[i] == 'C':
            complement[len(sequence)-i-1] = 'G'
        elif sequence[i] == 'G':
            complement[len(sequence)-i-1] = 'C'
        elif sequence[i] == 'T':
            complement[len(sequence)-i-1] = 'A'

    final = ''.join(complement)
    return final

def getProm(name):

    genes_f = open(mastercsvfile)
    genes = csv.reader(genes_f)
    direc = '0'

    for row in genes:
        if name in row[0]:
            start = pf.findP(name)
            direc = row[5]

    if direc == 'F':
        sequencef = findSeq([int(start)-PROM_LENGTH+1,int(start)],fastafile)
    elif direc == 'R':
        sequence = findSeq([int(start),int(start)+PROM_LENGTH-1],fastafile)
        sequencef = reVerse(sequence)
    else:
        print('This gene name is not in the system') #### bad error handling?
        sys.exit[1]

    return sequencef

def align(tfProm,geneProm):
    score = [0]*max(len(tfProm),len(geneProm))

    for i in range(min(len(tfProm),len(geneProm))):
        if i > 1:
            if tfProm[i] == geneProm[i]:
                score[i] = score[i-1] + MATCH
            else:
                if score[i-1] > THRESHOLD:
                    if score[i-2] > score[i-1]:
                        score[i] = score[i-1]
                    elif score[i-2] == score[i-1]:
                        score[i] = score[i-1]
                    else:
                        score[i] = score[i-1] + MISMATCH
                elif score[i-1] == 0:
                    score[i] = 0
                else:
                    if score[i-2] > score[i-1]:
                        score[i] = score[i-1] + MISMATCH
                    else: score[i] = 0
        elif i > 0:
            if tfProm[i] == geneProm[i]:
                score[i] = score[0] + MATCH
            else: score[i] = 0
        else:
            if tfProm[i] == geneProm[i]:
                score[i] = MATCH
            else: score[i] = 0 
    top = max(score)
    second = score.remove(max(score))
    return max(score),top

def ThirdParam(tfName,geneName):

    tfProm = getProm(tfName)
    geneProm = getProm(geneName)

    score = [0]*len(tfProm)
    for i in range(len(tfProm)):
        score[i] = align(tfProm[i:len(tfProm)]+tfProm[0:i],geneProm)
    
    fscore = max(score)
    finalscore = fscore[1]

    prob_f = open(thirdparamcsv)
    prob = csv.reader(prob_f)
    for row in prob:
        if str(finalscore) == row[0]:
            probyes = row[1]
            probno = row[2]

    return probyes, probno

def randSeq(length): # produces random sequence of given length
    seq = ''
    for i in range(length):
        num = random.randint(1,4)
        if num == 1: seq = seq + 'A'
        elif num == 2: seq = seq + 'C'
        elif num == 3: seq = seq + 'G'
        else: seq = seq + 'T'
    return seq

def randPair(tfProm,geneProm): # runs alignment on any two promoters

    score = [0]*len(tfProm)
    for i in range(len(tfProm)):
        score[i] = align(tfProm[i:len(tfProm)]+tfProm[0:i],geneProm)
    return max(score)

def generate(): # generates file from 5000 random sequence pairs
    n = 5000

    with open(output, "w") as f:
        for i in range(n):
            score = randPair(randSeq(200),randSeq(200))
            f.write("{},{}\n" .format(score[0],score[1]))
 
    return

