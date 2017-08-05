# python字典（dict）get方法 #

在获取字典值的时候，有两种方法，一种是通过dict['key']，另外一个就是dict.get()方法，通过键值访问并设置参数，相当于一个if elif else 判断语句

下面举例说明：

	info ={'apple':3,'pea':5,'banana':3}
	select = raw_input('input your choice:')
	print info.get(select,0)

如果输入的键值存在字典中，可以得到水果的数量，如果没有则显示数量为0