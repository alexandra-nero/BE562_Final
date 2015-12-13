import sys, csv, os

MASTERCSV = 'Ecoli_MG1655Master.csv'
GNOMELENGTH = 4639675
INTERGENEDIST = 25

def readcsv(file):
    file = open(file)
    file = csv.reader(file)
    T = []
    for row in file:
        T.append(row)
    return(T)

def getTnum(gene, csvmatrix):
    temp = []
    for i in range(len(csvmatrix)-1):
        if gene in csvmatrix[i][0]: 
            temp.append(i)
    if len(temp) == 0:
        return('Error: No occurences of gene \'' + gene + '\'.')
        sys.exit(1)
    elif len(temp) == 1:
        c = int(temp[0])
    else: 
        c = int(temp[0])
    return c

def findP(gene):
    csvfile = MASTERCSV
    pcutoff = INTERGENEDIST
    genomelength = GNOMELENGTH
    csvmatrix = readcsv(csvfile)
    position = getTnum(gene, csvmatrix)
    genenum = len(csvmatrix)
    
    if csvmatrix[position][5] == 'F' and csvmatrix[(position-1)%genenum][5] == 'F':
            #If query and target are more than pcutoff bp away, P is of query
            if int(csvmatrix[position][3]) > (int(csvmatrix[(position-1)%genenum][4])+pcutoff)%GNOMELENGTH:
                output = csvmatrix[position][3]
            #If are less than pcutoff away, go back until right 
            else:
                i, counter = 1, 0
                while i < 100 and counter == 0:
                    if csvmatrix[(position-1-i)%genenum][5] == 'R':
                        output = csvmatrix[(position-i)%genenum][3]
                        counter = 1
                    elif int(csvmatrix[(position-i)%genenum][3])%GNOMELENGTH > (int(csvmatrix[(position - i-1)%genenum][4])+pcutoff)%GNOMELENGTH:
                        output = csvmatrix[(position-i)%genenum][3]
                        counter = 1
                    else:
                        i += 1
        #If both query and target are R
    elif csvmatrix[position][5] == 'R' and csvmatrix[(position + 1)%genenum][5] == 'R':
            if int(csvmatrix[position][3]) < (int(csvmatrix[(position+1)%genenum][4])-pcutoff)%GNOMELENGTH:
                output = csvmatrix[position][3]
        #If are less than pcutoff away, go forward until right
            else:
                i, counter = 1, 0
                while i < 100 and counter == 0:
                    if csvmatrix[(position+i+1)%genenum][5] == 'F':
                        output = csvmatrix[(position+i)%genenum][3]
                        counter = 1
                    elif int(csvmatrix[(position+i)%genenum][3]) < (int(csvmatrix[(position+i+1)%genenum][4])-pcutoff)%GNOMELENGTH:
                        output = csvmatrix[(position+i)%genenum][3]
                        counter = 1
                    else:
                        i += 1
    elif csvmatrix[position][5] == 'F' and csvmatrix[(position-1)%genenum][5] == 'R':
        output = csvmatrix[position][3]

    elif csvmatrix[position][5] == 'R' and csvmatrix[(position+1)%genenum][5] == 'F':
        output = csvmatrix[position][3]
                
    else:
        return('Error: genome is confusing')
        sys.exit(1)    

    return output

