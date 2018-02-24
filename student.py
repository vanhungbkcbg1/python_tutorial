from lib.student import Student
from lib.Person import Person

a=Student()
print a.getName()
a.getName()

if( isinstance(a,Student)):
    print  'student'

if issubclass(Student,Person):
    print  'sub class of persio'