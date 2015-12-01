# -*- coding: cp936 -*-
#---------------------------------------------
#                                            -
#author  chile                            -
#version 1.0                               -
#since                                       -
#date  2014-02-17                                      -
#Desc KMP search string -
#                                            -
#                                            -
#                                            -
#---------------------------------------------

#On the string to pretreatment, find fails to match the substring fallback position
def preprocess(patter):
    length = len(patter)
    p = handlerList(length)
    j = -1
    p[0] = j 
    for i in range(1,length):
        j = p[i - 1]
        while j >= 0 and patter[i] != patter[j+1]:
            j = p[j]
        
        if patter[i] == patter[j+1]: #Having repeated characters, fallback position +1
            p[i] = j + 1
        else:
            p[i] = -1
    
    return p

#The initialization of a tuple
def handlerList(len,default = 0):
    if len <= 0:
        return
    p = []
    for i in range(len):
        p.append(default)
    return p

def kmp(value,pattern):
    srcSize = len(value)
    subSize = len(pattern)
    p = preprocess(pattern)
    tIndex , pIndex ,total = 0 , 0 , 0
    while tIndex <srcSize and pIndex <subSize: #Find the right back position
        if (value[tIndex] == pattern[pIndex]):
            tIndex += 1
            pIndex += 1
        elif pIndex == 0:
            tIndex += 1
        else:
            pIndex = p[pIndex - 1] + 1
       
        if pIndex == subSize:  #The output matching results, and make comparison to continue
            pIndex = 0
            total += 1
            print 'find',pattern,'at',(tIndex - subSize)
    print 'find times ' , total

    
var = 'abadfafdewefwfafd'
pattern ='faf'
kmp(var,pattern)