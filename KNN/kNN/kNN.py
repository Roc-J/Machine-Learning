# -*- coding:utf-8 -*-
# author:Roc-J

from numpy import *
import operator
from os import listdir

'''kNN算法的通用算法'''
def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels =['A','A','B','B']
    return group,labels

# 构造的第一个分类器
def classify(intX,dataSet,labels,k):
    # 使用欧式距离公式
    # 得到数据集的第一维度
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistances = distances.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistances[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

# 将文本记录转换为Numpy的解析程序
def file2matrix(filename):
    fileReader = open(filename)
    arrayLines = fileReader.readlines()
    numberOfLines = len(arrayLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector =[]
    index = 0
    for line in arrayLines:
        line = line.strip()
        listFormLine = line.split('\t')
        returnMat[index,:]= listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))
        index +=1
    return returnMat,classLabelVector

# 归一化特征值
def autoNorm(dataSet):
    # dataSet.min(0)中的参数0使得函数可以从列中选取最小值，而不是选取当前行的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet /tile(ranges,(m,1))
    return normDataSet,ranges,minVals

# 分类器针对约会网站的测试代码
def datingClassTest():
    rateTest = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*rateTest)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],5)
        print 'the classifier came back with %d，the real answer is %d' % (classifierResult,datingLabels[i])
        if(classifierResult!=datingLabels[i]):
            errorCount+=1
    print 'the total error rate is : %f' %(errorCount/float(numTestVecs))


# 使用算法，构建完整可用系统
def classifyPerson():
    resultList = ['不喜欢','一般喜欢','很喜欢']
    percentTats = float(raw_input('percentage of time spent palying video games?'))
    ffMiles = float(raw_input('frequent flier miles earned per year?'))
    iceCream = float(raw_input('liters of ice cream consumed per yaer?'))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inputArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify((inputArr-minVals)/ranges,normMat,datingLabels,5)
    print '你对这个人的评价是',resultList[classifierResult-1]

# 下面的内容是手写识别系统
# 图像转换为测试向量
def img2vector(filename):
    returnVect = zeros((1,1024))
    fileReader = open(filename)
    for i in range(32):
        lineStr = fileReader.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

# 使用k-近邻算法识别手写数字

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumberStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumberStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumberStr = int(fileStr.split('_')[0])
        vecUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify(vecUnderTest,trainingMat,hwLabels,3)
        print 'the classifier came back with %d,the real answer is %d' % (classifierResult,classNumberStr)
        if(classifierResult!=classNumberStr):
            errorCount+=1.0
    print 'the total number of errors is %d' % errorCount
    print 'the total error rate is : %f' % (errorCount/float(mTest))