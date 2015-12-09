#here is where the code to properly identify the third parameter
#COMMON MOTIFS now uses sequence alignment to find the probability based on the motif

import csv

mastercsvfile = 'testcsv.csv'
fastafile = 'sequence.fasta'
PROM_LENGTH = 200
THRESHOLD = 2
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

  for row in genes:
      if name in row[0]:
          start = int(row[6]) # promoter start from pfinder.py
          direc = row[5]

  if direc == 'F':
      sequencef = findSeq([start-PROM_LENGTH+1,start],fastafile)
  elif direc == 'R':
      sequence = findSeq([start,start+PROM_LENGTH-1],fastafile)
      sequencef = reVerse(sequence)
  else:
      print('This gene name is not in the system') #### bad error handling?
      sys.exit(1)

  print(sequencef)
  return sequencef

def SecondParam(tfName,geneName):

  tfProm = getProm(tfName)
  geneProm = getProm(geneName)


  return

