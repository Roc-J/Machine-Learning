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

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList

def apriori(dataSet,minSupport=0.5):
    C1 = createC1(dataSet)
    D = map(set,dataSet)
    L1,supportData = scanD(D,C1,minSupport)
    L = [L1]
    k=2
    while(len(L[k-2])>0):
        Ck = aprioriGen(L[k-2],k)
        Lk,supK =scanD(D,Ck,minSupport)
        supportData.update(supK)
        L.append(Lk)
        k +=1
    return L,supportData

# 关联规则生成函数
def generateRules(L,supportData,minConf=0.7):
    bigRules = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if(i>1):
                rulesFromConseq(freqSet,H1,supportData,bigRules,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRules,minConf)
    return bigRules

def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq]
        if conf >=minConf:
            print freqSet-conseq,'--->',conseq,'conf',conf
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    m = len(H[0])
    if(len(freqSet)>(m+1)):
        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet,Hmp1,supportData,brl,minConf)
        if(len(Hmp1)>1):
            rulesFromConseq(freqSet,Hmp1,supportData,brl,minConf)