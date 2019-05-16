#-*-coding:utf-8-*-

# pass 是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句

class Animal(object):
    pass
class Dog(Animal):
    def __init__(self,name):
        self.naem = name
class Cat(Animal):
    def __init__(self, name): 
        ## 定义name属性
        self.name = name
    
class Person(object):
    def __init__(self, name): 
        ## 定义name和pet属性 
        self.name = name
        ## Person has-a pet of some kind 
        self.pet = None
## ??
class Employee(Person):
    def __init__(self, name, salary): 
        # super 用于调用父类(超类)的一个方法。
        # 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题
        # super(Class, self).xxx :
        super(Employee, self).__init__(name) 
        ## salary属性
        self.salary = salary

## ??
class Fish(object): 
    pass
## ??
class Salmon(Fish): 
    pass
## ??
class Halibut(Fish): 
    pass


## rover is-a Dog
rover = Dog("Rover")
## ??
satan = Cat("Satan")
## ??
mary = Person("Mary")
## 复制给对象的属性
mary.pet = satan
## ??
frank = Employee("Frank", 120000)
## ??
frank.pet = rover
## ??
flipper = Fish()
## ??
crouse = Salmon()
## ??
harry = Halibut()