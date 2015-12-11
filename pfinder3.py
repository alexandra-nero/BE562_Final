
import sys, csv, os

MASTERCSV = 'testcsv.csv'
GNOMELENGTH = 20000
INTERGENEDIST = 200

def readcsv(file):
    file = open(file)
    file = csv.reader(file)
    T = []
    for row in file:
        T.append(row)
    return(T)

def getTnum(gene, csvmatrix):
    temp = []
    for i in range(1, len(csvmatrix)):
        if gene in csvmatrix[i][0]: #if gene in the string at csv[i][0], there's more than one name
            temp.append(i)
    if len(temp) == 0:
        return('Error: No occurences of gene \'' + gene + '\'.')
        sys.exit(1)
    elif len(temp) == 1:
        c = temp[0]
    else: 
        return('Error: ' + str(len(temp)) + ' occurences of gene \'' + gene + '\'.')
        sys.exit(1)
    return c

def findP(gene, csvfile, pcutoff, genomelength):
    csvmatrix = readcsv(csvfile)
    position = getTnum(gene, csvmatrix)
    
    if csvmatrix[position][5] == 'F' and csvmatrix[position-1][5] == 'F':
            #If query and target are more than pcutoff bp away, P is of query
            if int(csvmatrix[position][3]) > int(csvmatrix[position-1][4])+pcutoff:
                output = csvmatrix[position][3]
            #If are less than pcutoff away, go back until right 
            else:
                i, counter = 1, 0
                while i < 100 and counter == 0:
                    if csvmatrix[position-1-i][5] == 'R':
                        output = csvmatrix[position-i][3]
                        counter = 1
                    elif int(csvmatrix[position-i][3]) > int(csvmatrix[position - i-1][4])+pcutoff:
                        output = csvmatrix[position-i][3]
                        counter = 1
                    else:
                        i += 1
        #If both query and target are R
    elif csvmatrix[position][5] == 'R' and csvmatrix[position + 1][5] == 'R':
            if int(csvmatrix[position][3]) < int(csvmatrix[position+1][4])-pcutoff:
                output = csvmatrix[position][3]
        #If are less than pcutoff away, go forward until right
            else:
                i, counter = 1, 0
                while i < 100 and counter == 0:
                    if csvmatrix[position+i+1][5] == 'F':
                        output = csvmatrix[position+i][3]
                        counter = 1
                    elif int(csvmatrix[position+i][3]) < int(csvmatrix[position+i+1][4])-pcutoff:
                        output = csvmatrix[position+i][3]
                        counter = 1
                    else:
                        i += 1
    elif csvmatrix[position][5] == 'F' and csvmatrix[position-1][5] == 'R':
        output = csvmatrix[position][3]

    elif csvmatrix[position][5] == 'R' and csvmatrix[position+1][5] == 'F':
        output = csvmatrix[position][3]
                
    else:
        return('Error: genome is confusing')
        sys.exit(1)    

    return output
                    
#have to add the addition of the promoter to the end of the csv file       
                
x = findP('yaaA', MASTERCSV, INTERGENEDIST, GNOMELENGTH)

