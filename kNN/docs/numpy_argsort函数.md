# numpy函数-argsort()函数 #

函数argsort在模块numpy.core.fromnumeric中，该函数是返回排序数组的索引

函数定义是:
	
	argsort(a,axis=-1,kind='quicksort',order=None)

参数说明：

	a:array_like，数组排序的
	axis:int或None，是可选项，是维度排序，默认是最后一维排序。如果没有，使用扁平排序
	kind:{'quicksort','mergesort','heapsort'}，指明的是排序算法
	order:str或str的列表，可选，根据a是否是有定义的字段来决定比较的

	返回值是沿指定的轴（维度）排序的a的索引数组

举例说明：

	>>>import numpy
	>>> x = numpy.array([3,1,2])
	>>> numpy.argsort(x)
	array([1, 2, 0])
	
引入numpy后，可以使用numpy创建一个数组，然后使用numpy.argsort(x)将x进行排序，返回排序后的索引大小，访问的时候，通过x[1],x[2],x[0]来访问1,2,3

