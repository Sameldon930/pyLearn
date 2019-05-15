# -*-coding:utf-8-*-
# 创建三个列表 存到变量中
the_count = [1,2,3,4,5]
fruits = ['apple','orange','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# 循环五次 每次输出一组fruits这个列表
for number in the_count:
    print number,fruits
    
# 类似于遍历 change这个列表中的每个元素 并输出
for  i in change :
    print i
    
# 定义一个空列表
elements = []

# 循环一个范围的数字 并将每一个元素放到上面定义的空列表中

# range(10)        # 从 0 开始到 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 11)     # 从 1 开始到 11
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range(0, 30, 5)  # 步长为 5
# [0, 5, 10, 15, 20, 25]
# range(0, 10, 3)  # 步长为 3
# [0, 3, 6, 9]
# range(0, -10, -1) # 负数
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# range(0)
# []
# range(1, 0)
# []


for i in range(0,6):
    print "Adding %d to the list." % i 
    # 放到新的列表中
    elements.append(i)
# 遍历新的列表的内容 
for i in elements:
    print i