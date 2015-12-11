
import sys, csv, os

MASTERCSV = 'testcsv.csv'
GNOMELENGTH = 20000
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
    for i in range(1, len(csvmatrix)):
        if gene in csvmatrix[i][0]: #if gene in the string at csv[i][0], there's more than one name
            temp.append(i)
    if len(temp) == 0:
        return('Error: No occurences of gene \'' + gene + '\'.')
        sys.exit(1)
    elif len(temp) == 1:
        return(temp[0])
    elif len(temp) > 1:
        return('Error: ' + str(len(temp)) + ' occurences of gene \'' + gene + '\'.')
        sys.exit(1)

def findP(gene, csvfile, pcutoff, genomelength):
    csvmatrix = readcsv(csvfile)
    position = getTnum(gene, csvmatrix)
    
    
    if csvmatrix[positon][5] == 'F' and csvmatrix[positon-1][5] == 'F':
            #If query and target are more than pcutoff bp away, P is of query
            if int(csvmatrix[positon][3]) > int(csvmatrix[positon-1][4])+pcutoff:
                output = csvmatrix[positon][3]
            #If are less than pcutoff away, go back until right 
            else:
                i, counter = 1, 0
                while i < 100 and counter == 0:
                    if csvmatrix[positon-1-i][5] == 'R':
                        output = csvmatrix[positon-i][3]
                        counter = 1
                    elif int(csvmatrix[positon-i][3]) > int(csvmatrix[positon - i-1][4])+pcutoff:
                        output = csvmatrix[positon-i][3]
                        counter = 1
                    else:
                        i += 1
        #If both query and target are R
    elif csvmatrix[positon][5] == 'R' and csvmatrix[positon + 1][5] == 'R':
            if int(csvmatrix[positon][3]) < int(csvmatrix[positon+1][4])-pcutoff:
                output = csvmatrix[positon][3]
        #If are less than pcutoff away, go forward until right
            else:
                i, counter = 1, 0
                while i <100 and counter == 0:
                    #if past the bottom of the list--stop
                    if (positon-i+1) == len(csvmatrix):                        
                        return()
                    #if the next gene is in opposite orientation, take current
                    #promoter
                    elif csvmatrix[positon+i+1][5] == 'F':
                        return(csvmatrix[positon+i][0])
                    #if promoter is of right length, take it
                    elif int(csvmatrix[positon+i][3]) < int(csvmatrix[positon+i+1][4])-pcutoff:
                        return(csvmatrix[positon+i][0])
                    i += 1
    elif csvmatrix[positon][5] == 'F' and csvmatrix[positon-1][5] == 'R':
        output = csvmatrix[position][3]

    elif csvmatrix[positon][5] == 'R' and csvmatrix[positon+1][5] == 'F':
        output = csvmatrix[position][3]
                
    else:
        return('Error: genome is confusing')
        sys.exit(1)    

    return output
                    
#have to add the addition of the promoter to the end of the csv file       
                
x = findP('Gene 5', MASTERCSV, INTERGENEDIST, GNOMELENGTH)

