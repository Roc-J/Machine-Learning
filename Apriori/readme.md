# 使用Apriori算法进行关联分析 #

## 示例：发现毒蘑菇的相似特征 ##

在这个例子中，寻找毒蘑菇中的一些公共特征，利用这些特征就能避免吃到那些有毒的蘑菇。UCI的机器学习数据集合中有一个关于肋形蘑菇的23种特征的数据集，每一个特征都包含了一个标称数据值，必须将这些标称值转化为一个集合。幸运的是，已经有人做好了这种转换。Roberto Bayardo对UCI蘑菇数据集进行了解析，将每个蘑菇样本转换成一个特征集合。其中，枚举了每个特征的所有可能值，如果某个样本包含特征，那么该特征对应的整数值被包含在数据集中。  

它在源数据集合中是一个名为mushroom.dat的文件

可以打开文件mushroom.dat查看

第一个特征表示有毒或者可食用。如果某样本有毒，则值为2。如果可食用，则值为1。下一个特征是蘑菇伞的形状，有六种可能的值，分别用整数3-8来表示。

* 文件mushroom.dat的每一行第一个特征用1或者2表示可食用或有毒，其余列都是某种蘑菇的特征。通过apriori算法寻找包含特征值为2的频繁项集。

当前目录下程序运行：

	import apriori
	mushDatSet = [line.split() for line in open('mushroom.dat').readlines()]
	L, suppData = apriori.apriori(mushDatSet, minSupport = 0.3)

	在结果中搜索包含有毒特征值2的频繁项集：
	for item in L[1:
		if item.intersection('2'): print item

	
![](http://i.imgur.com/vJ3YEIK.png)


	对更大的项目来重复上述过程：

	for item in L[3]:
		if item.intersection('2'): print item

![](http://i.imgur.com/43pyNKK.png)

接下来你需要观察一下这些特征，以便知道了解野蘑菇的那些方面。如果看到其中任何一个特征，那么这些蘑菇就不要吃了。
