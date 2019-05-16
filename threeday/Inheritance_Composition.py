#-*-coding:utf-8-*-

# 继承  合成


# 隐式继承  
# 父类里定义了一个函数，但没有在子类中定义的例子，这时候会发生隐式继承
class Parent(object):#父类
    def implicit(self):
        print "PARENT implicit()"
class Child(Parent):#子类继承父类
    pass

# 实例化父类
dad = Parent()
# 实例化子类
son = Child()

# 调用方法
# dad.implicit() PARENT implicit()
# son.implicit() PARENT implicit()
#####################################################################################

# 显式重写
# 让子类里的函数有一个不同的行为，这种情况下隐式继承是做不到的，
# 而你需要覆写子类中的函数，从而实现它的新功能。
# 你只要在子类 Child 中定义一个相同名称的函数就可以了
class Parent(object):
    def override(self):
        print "PARENT override()"
class Child(Parent):
    def override(self):
        print "Child override()"

dad = Parent()
son = Child()

# 调用方法
# dad.override() PARENT override()
# son.override() Child override()

#####################################################################################

class Parent(object):
    def altered(self):
        print "PARENT altered() "
class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"#父类变化前
        super(Child,self).altered() #此时调用的方法是 child的父类的方法altered()
        print "CHILD, AFTER PARENT altered()"#父类变化后
        
dad = Parent()
son = Child()

# dad.altered()   PARENT altered() 
# son.altered()   PARENT altered() 
        
#####################################################################################
# 最终版本

class Parent(object):
    def override(self):
        print "PARENT override()"
    def implicit(self):
        print "PARENT implicit()"
    def altered(self):
        print "PARENT altered()"
class Child(Parent):
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE PARENT altered()" 
        super(Child, self).altered() 
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

# 子类没有这个方法 就会继承父类的方法
# dad.implicit() # PARENT implicit()
# son.implicit() # PARENT implicit()

# # 子类有和父类同名的方法 所以会单独输出
# dad.override()  # PARENT override()
# son.override()  # CHILD override()

# # 子类中用super方法 会调用到父类的方法
# dad.altered()  # PARENT altered()
# son.altered()  # PARENT altered()

#####################################################################################


# 合成

class Other(object):
    def override(self):
        print "other override()"
    def implicit(self):
        print "ohter implicit()"
    def altered(self):
        print "other altered()"
        
class Child(object):
    def __init__(self):
        # 在这里就开始实例化上面的Other对象
        self.other = Other()
    def implicit(self):
        # 调用上面对象的implicit方法
        self.other.implicit()
    def override(self):
        print "Child override()"
    def altered(self):
        print "CHILD, BEFORE OTHER altered()" 
        # 调用上面对象的altered方法
        self.other.altered() 
        print "CHILD, AFTER OTHER altered()"
    
son = Child()

son.implicit() #ohter implicit()
son.override() #Child override()
son.altered()  #other altered()