# Python_sorted函数 #

	>>> help(sorted)
	Help on built-in function sorted in module __builtin__:
	
	sorted(...)
	    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

sorted是内建函数

函数定义：	

	sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
	参数说明：
	iterabele ： 是可迭代的类型
	cmp ：用于比较的函数，比较什么由key决定，有默认值，迭代集合中的一项
	key : 用列表元素的某个属性和函数作为关键字，有默认值，迭代集合中的一项
	reverse ：排序规则，reverse=True或reverse=False，有默认值
	返回值: 是一个经过排序的可迭代类型，和Iterable一样

> 提示，一般来说，cmp和key可以使用lambda表达式

sorted与sort函数不同的是，sort是在原位置重新排列列表，而sorted（)是产生一个新的列表

## 基本排序 ##

	>>> print sorted([1,2,3,6,5,4])
	[1, 2, 3, 4, 5, 6]

## cmp参数排序 ##

	>>> L = [('b',2),('a',5),('c',1),('d',4)]
	>>> print sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))
	[('c', 1), ('b', 2), ('d', 4), ('a', 5)]
	>>> print sorted(L, cmp=lambda x,y:cmp(x[0],y[0]))
	[('a', 5), ('b', 2), ('c', 1), ('d', 4)]

## key参数排序 ##
	
	>>> print sorted(L, key=lambda x:x[1])
	[('c', 1), ('b', 2), ('d', 4), ('a', 5)]

## reverse参数排序 ##

	>>> print sorted([1,2,3,6,5,4], reverse=True)
	[6, 5, 4, 3, 2, 1]
	>>> print sorted([1,2,3,6,5,4], reverse=False)
	[1, 2, 3, 4, 5, 6]

