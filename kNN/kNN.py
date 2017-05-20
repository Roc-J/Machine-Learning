# -*- coding:utf-8 -*-
# author:Roc-J

from numpy import *
import operator

'''kNN算法的通用算法'''
def createDateSet():
    group = array([[1.0,1,1],[1.0,1.0],[0,0],[0,0.1]])
    labels =['A','A','B','B']
    return group,labels

def classify(intX,dataSet,labels,k):
    # 使用欧式距离公式
    # 得到数据集的第一维度
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5




