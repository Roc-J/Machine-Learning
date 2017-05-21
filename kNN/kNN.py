# -*- coding:utf-8 -*-
# author:Roc-J

from numpy import *
import operator

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


