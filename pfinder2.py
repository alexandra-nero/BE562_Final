# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:29:42 2015

@author: R
"""

import sys, csv, os

def readcsv(file):
    file = open(file)
    file = csv.reader(file)
    T = []
    for row in file:
        T.append(row)
    return(T)

def getTnum(gene, csv):
    temp = []
    for i in range(1, len(csv)):
        if gene in csv[i][0]: #if gene in the string at csv[i][0], there's more than one name
            temp.append(i)
    if len(temp) == 0:
        return('Error: No occurences of gene \'' + gene + '\'.')
    elif len(temp) == 1:
        return(temp[0])
    elif len(temp) > 1:
        return('Error: ' + str(len(temp)) + ' occurences of gene \'' + gene + '\'.')

def findP(gene, csv, pcutoff, genomelength):
    temp = getTnum(gene, csv)
    temp = temp + int(len(csv))
    #loops around genome 
    subT = csv[0:len(csv)]
    supT = csv[1:len(csv)]
    
    for i in range(0, len(supT)):
        subT[i+1][4] =  (0 - genomelength) + int(subT[i+1][4])
        subT[i+1][3] =  (0 - genomelength) + int(subT[i+1][3])
        supT[i][4] =  (genomelength) + int(supT[i][4])
        supT[i][3] =  (genomelength) + int(supT[i][3])
    
    csv = subT + T[1:len(csv)] + supT
   
    if len(str(temp)) == 1:
        #If both query and target are F
        if csv[temp][5] == 'F' and csv[temp-1][5] == 'F':
            #If query and target are more than pcutoff bp away, P is of query
            if int(csv[temp][3]) > int(csv[temp-1][4])+pcutoff:
                return(csv[temp][0])
            #If are less than pcutoff away, go back until right 
            elif int(csv[temp][3]) <= int(csv[temp-1][4])+pcutoff:
                i, counter = 1, 0
                while i < 100 and counter == 0:
                    #if get to the top of the list--, edit                     
                    if (temp-1-i) == 0:
                        return()
                    #if previous gene is in opposite orientation, take current
                    #promoter
                    elif csv[temp-1-i][5] == 'R':
                        return(csv[temp-i][0])
                    #If promoter is of right length, take it
                    elif int(csv[temp-i][3]) > int(csv[temp - i-1][4])+pcutoff:
                        return(csv[temp-i][0])
                    i += 1
        #If both query and target are R
        if csv[temp][5] == 'R' and csv[temp + 1][5] == 'R':
            if int(csv[temp][3]) < int(csv[temp+1][4])-pcutoff:
                return(csv[temp][0])
        #If are less than pcutoff away, go forward until right
            elif int(csv[temp][3]) >= int(csv[temp+1][4])-pcutoff:
                i = 1
                while i <100:
                    #if past the bottom of the list--stop
                    if (temp-i+1) == len(csv):                        
                        return()
                    #if the next gene is in opposite orientation, take current
                    #promoter
                    elif csv[temp+i+1][5] == 'F':
                        return(csv[temp+i][0])
                    #if promoter is of right length, take it
                    elif int(csv[temp+i][3]) < int(csv[temp+i+1][4])-pcutoff:
                        return(csv[temp+i][0])
                    i += 1
                
                    
                    
#have to add the addition of the promoter to the end of the csv file       
                

T = readcsv('C:/python/test.csv')
x = findP('Gene 5', T, 25, 1000)






 
