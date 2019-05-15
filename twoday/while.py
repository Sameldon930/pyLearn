#-*- coding:utf-8-*-

i = 0
numbers = []

# 循环 i 自增+1 在小于6的时候 将值存到numbers列表中
while i < 6 :
    # print "At the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now: ", numbers 
    # print "At the bottom i is %d" % i
print "The numbers: "

# 遍历numbers这个列表
for num in numbers:
    print num
    
    