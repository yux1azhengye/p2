#!/usr/bin/python
# -*- coding: UTF-8 -*-
import copy

class Employee(object):
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print  ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print  ("Name : ", self.name, ", Salary: ", self.salary)

# class Rookie(Employee):  #菜鸟继承员工类
#     pass
# #因为是继承的职工类，所以菜鸟类可以直接使用职工类的方法
# xiaowang = Rookie("小王","5000")
# xiaowang.displayEmployee()
# xiaowang.displayCount()

#类的多态：在这里我给菜鸟类的displayEmployee函数重新定义
class Rookie(Employee):
    def displayEmployee(self):
        print  ("一只职场菜鸟","Name : ", self.name, ", Salary: ", self.salary)
xiaowang = Rookie("小王","5000")
# xiaowang.displayEmployee()

#复制对象

print("小王1:",xiaowang)
#1.直接引用复制
xiaowang2 = xiaowang
print("小王2:",xiaowang2)
xiaowang2.displayEmployee()
xiaowang2.displayCount()
#2.copy()方法复制
xiaowang3 = copy.copy(xiaowang)
print("小王3:",xiaowang3)
xiaowang3.displayEmployee()
xiaowang3.displayCount()
#3.deepcopy()方法 深度复制
xiaowang4 = copy.deepcopy(xiaowang)
print("小王4:",xiaowang4)
xiaowang4.displayEmployee()
xiaowang4.displayCount()