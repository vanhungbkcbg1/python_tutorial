import numpy as np
import calendar
from lib.student import Student
# from student import hello
from  file import writeFile
from  file import readFile
from handleexcepttion import doSomething
import logging
value =1
print("hello world")
if(value==1):
    print("value equal 1")
elif (value==2):
    print("value equal 2")
else:
    print("diff value")
	
def myfunction(name,age):
    print("name=%s age=%s"%(name,age))
myfunction("vanhung",27)



list={1,2,3,4,4}
tupe=(1,2,3)
print(list)
print(tupe)

dict={}
dict['name']="dsfdsfds"
dict={"name":"vanhung",'age':"1"}

print(dict['name'])
print(dict['age'])
floatx=float(1)
print(dict)
print(floatx)

# len of string
print(len("hello"))
str="hello"
print(str[1:3])

# hello()
writeFile("hello")

readFile()
doSomething()
logger=logging.getLogger(__name__)
logger.exception("e")

str="hello"
print(str[4])
print(str[1])
print(str[1:2])

for i in list:
    print(i)

for letter in "pythfdsfdsfdsfsfdson":
    print(letter)

student= Student()
student.doSomething()



