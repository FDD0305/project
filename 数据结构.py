s='helloworld'
l='hi'
#索引
#正向递增
for i in range (0,len(s)):#range用法且注意正向从0到n-1
    print(i,s[i],end='\t\t')
print('\n---------------------')
#反向递减
for i in range(-10,0):#反向从-N到-1
    print(i,s[i],end='\t\t')
print('\n-----------------------')
#切片操作
s1=s[0:5:2]
print(s1)
s2=s[::-1]#逆序输出字符串
print(s2)
#序列相加相乘
print(l+s)
print(l*5)
#序列操作函数
print('e在helloworld中存在吗?',('e'in s))#注意加括号
#列表
#创建列表
lst=['hello','world',98,100.5]
lst2=list('helloworld')
#列表是序列中的一种，对序列的操作符，运算符，函数均可使用
#删除列表del list
#遍历列表
for item in lst:
    print(item)
for i in range(0,len(lst)):
    print(lst[i])
for index,item in enumerate(lst,2):
    print(index,item)






