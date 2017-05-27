# -*- coding:utf-8 -*-
# Author: Roc-J

'''创建一个数据集'''
def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

'''构建候选项集合'''
def createC1(dataset):
    C1=[]
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    C1.sort()
    return map(frozenset,C1)

'''返回包含支持度值的字典'''
def scanD(dataSet,Ck,minSupport):
    ssCnt = {}
    for transaction in dataSet:
        for can in Ck:
            if can.issubset(transaction):
                if not ssCnt.has_key(can):
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1

    # 将数值转换成float，后面要进行除法
    numItem = float(len(dataSet))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItem
        if support >=minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList,supportData

