#-*- coding:utf-8-*-
def add(a,b):
    print "ADDING %d + %d"%(a,b)
    return a + b
def subtract(a,b):
    print "subtract %d - %d"%(a,b)
    return a - b
def multiply(a,b):
    print "multiply %d * %d"%(a,b)
    return a * b
def divide(a,b):
    print "divide %d / %d"%(a,b)
    return a / b
        
print "Let's do some math with just functions!"

# 调用函数 并将函数中的返回值传到变量
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
    age, height, weight, iq
)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

