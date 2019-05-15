#-*-coding:utf-8-*-
print "Let's practice everything."
print """
You\'d need to know 
\'bout escapes with 
\\ that do \n 
newlines and \t tabs.
"""

poem = """ \tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. 
"""
print "--------------" 
print poem
print "--------------"

five  = 10-2+3-6
print "this should be five: %s"%five  #5

# 定义函数 进行计算 赋值给三个属性 并返回这三个属性值
def secret_formula(started):
    jelly_beans = started * 500 
    jars = jelly_beans / 1000 
    crates = jars / 100 
    return jelly_beans, jars, crates

# 定义一个变量 调用函数  将函数返回的结果赋值给新的变量
start_point = 10000
# 返回的三个值赋值给三个变量
beans,jar,scrates =  secret_formula(start_point)


print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

start_point = start_point / 10
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
