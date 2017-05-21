# operator_itemgetter()函数 #

operator的itemgetter()函数是一个内建函数，用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）

	>>> a = [1,2,3]
	>>> b = operator.itemgetter(1)
	>>> b
	<operator.itemgetter object at 0x038AD830>
	>>> b(a)
	2


> 注意，operator.itemgetter(）获取的不是值，而是定义了一个函数，通过该函数作用到对数上才能获取值