#METHOD OVERRIDING:
# class manager:
#   def __init__(self,name,salary):
#     self.name=name
#     self.salary=salary
#     def showval(self):
#       return self.salary
# class emp(manager):
#   def __init__(self,name,salary,incentive):
#     super().__init__(name,salary)
#     self.incentive=incentive
#   def showval(self):
#     print(self.name)
#     return  self.salary+self.incentive

#1SUPER METHOD TO EXTEND FUCTIONALITY OF PARENT METHOD
# e=emp("chinmayee",10000000,1000000)
# print(e.showval())

# class name:
#   def info(self):
#     print("my name is rashmi")
# class gender(name):
#   def info(self):
#     super().info()
#     print("i am a girl")

# n=name()
# print(n.info())
# g=gender()
# print(g.info())


#OPERATOR OVERLOADING:
# class vector:
#   def __init__(self,i,j,k):
#     self.i=i
#     self.j=j
#     self.k=k
#   def __str__(self):
#     return f"{self.i}i+{self.j}j+{self.k}k"
#   def __add__(self,x):
#     return vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
# v1=vector(1,2,3)
# print(v1)
# v2=vector(9,7,3)
# print(v2)
# print(v1+v2)
# print(type(v1+v2))

#TIME MODULE:
# import time
# print(time.time())
# print("Readable form of time:\n",time.ctime(time.time()))
# print("Take a 3sec break")
# time.sleep(3)
# # print("3 secs done")
# print(time.strftime("%Y %M %D  %H %M %S"))
# # TO SCHEDULE TIME INSTEAD OF SLEEP FUNCTION:
# from datetime import datetime
# target_time="5:00:00"
# while True:
#   current_time=datetime.now().strftime("%H %M %S")
#   if current_time==target_time:
#     print("TIME TO WAKE UP AND STUDY")
#   else:
#     print("not yet")
#     break
#   time.sleep(1)
# print(datetime.now)


# ENUMERATE FUNCTIONS
# lst=[100,90,80]
# for i , num in enumerate(lst):
#   print(i,num)


#reverse a string
# str="abcdefgh"
# for i in reversed(str):
#   print(i)

# DICTIONARY
# stu={"name":"chinmayee","roll":12,"grade":1}
# for key in stu:
#   print(key)
# for value in stu.values():
#   print(value)
# for key,value in stu.items():
#   print(key,":",value)

# SPEACIAL CONTAINER DATATYPES:
# COUNTER():
from collections import ChainMap
d1={"a":10,"b":5}
d2={"b":25}
d3={"b":35,"c":5}
cm=ChainMap(d1,d2,d3)
print("Original chainmap:\n",cm)
print("Original maps or dicts:\n",cm.maps)#returns a list
cm["b"]=100
print(d1) # no updates in d2 and d3
cm["c"]=16
print(d1)
d4={"z":100}
new_cm=cm.new_child(d4)
print("new chainmap",new_cm)
print(new_cm["a"]) #searching for a key
new_cm['a']=294
print(new_cm["a"])
