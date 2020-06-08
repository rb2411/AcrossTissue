#plot each column in a different color in a scatter plot, assume the first line is the header


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
import validator
headers=[]
inputFile="/home/lu/AcrossTissue/ComparisonLSG/selectionParameterBetweenLS.csv"


#format: first line should be the header, each column is a list
def parseInputFile(fname):
    csvMatrix=[]
    f=open(fname)
    lines=f.readlines()
    global headers
    print lines[0]
    headers=lines[0].rstrip().split(",")
    for line in lines[1:]:
        splitList=line.rstrip().split(",")
        
        csvMatrix.append(splitList)
    return csvMatrix



def convertMatirxFromStringToFloat(matrix):
    newMatrix=[]
    for ls in matrix:
        floatList = list(map(float, ls)) 
        newMatrix.append(floatList)
    return newMatrix

csvMatrix=parseInputFile(inputFile)


matrix=np.transpose(np.asarray(csvMatrix))
        
AANames=matrix[0]    
codonNames=matrix[1]
matrix=matrix[2:]
matrix=convertMatirxFromStringToFloat(matrix)

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None


def getMedianListFromMatrix(matrix,transpose=False):
    medianList=[]
    if transpose:
        matrix=np.transpose(matrix)
    for ls in matrix:
        median=np.median(ls)
        medianList.append(median)
    return medianList

def getMeanListFromMatrix(matrix,transpose=False):
    meanList=[]
    if transpose:
        matrix=np.transpose(matrix)
    for ls in matrix:
        mean=np.mean(ls)
        meanList.append(mean)
    return meanList







#works, but the proportion is not clear in visualization
def plotMatrixInScatter(matrix):
    fig=plt.figure()
    plotGroupLS=[]
    meanList=getMeanListFromMatrix(matrix,transpose=True)
    medianList=getMedianListFromMatrix(matrix,transpose=True)
    corelation=validator.testCorelation(medianList,meanList,"pearson" )
    if corelation<0.99:
        print "Warning! Mean and Median has a corelation less than 0.99, choice of mean of median might make a difference"
    plotMean=plt.bar(range(1,len(medianList)+1),medianList)
    plotGroupLS.append(plotMean)
    
    for ls in matrix:
        plotGroup=plt.bar(range(1,len(ls)+1),ls)
        plotGroupLS.append(ls)
    
    global codonNames
    labelList=[]
    for s in codonNames:
        newS=""
        for c in s:
            newS+=c
            newS+="\n"
        labelList.append(newS)
    plt.xticks(range(1,len(medianList)+1),labelList,rotation=-5, fontsize=5)
    plt.show()
    fig.savefig("test.pdf",bbox_inches='tight')

plotMatrixInScatter(matrix)














