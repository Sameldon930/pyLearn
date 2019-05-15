#-*- coding:utf-8-*-
#实参和形参名字可以不相同

#定义函数 两个参数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count 
    print "You have %d boxes of crackers!" % boxes_of_crackers 
    print "Man that's enough for a party!" 
    print "Get a blanket.\n"
print "We can just give the function numbers directly:"
# 调用函数 传了两个参数的值是 20 30
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# 先定义两个变量 当作参数 进行调用函数传入
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
# 两个参数分别是算术表达式
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
# 两个参数分别是变量和整数相加
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

