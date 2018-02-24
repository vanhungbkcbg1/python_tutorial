from .Person import Person

from .. import *


class Student(Person):
    name = ''

    def __init__(self):

        Person.__init__(self,'hungnv')


    def getName(self):
        return Person.getName(self)+'Student'

    def helloWorld(self):
        print('hello world')
        self.doSomething()
        print(self.name)
        self.work()
        self.doFormat()
        self.test(name='vanhungkbcbg1')

    def work(self):
        len = 100
        for num in range(0, len):
            if (num == 2):
                pass
                print(num)
            else:
                print(int(1) + num)

    def doFormat(self):
        print('hello {name}'.format(name=self.name))

    def test(self, name="hungnv"):
        print(name)
