import numpy as np


a = np.array([
    (1,2),
    (4,5),
    (4,5),
    (4,5)])
print a.shape
# change shape from 3X3 ->
print a
a.reshape(2,4)
print a
# print a[0][0]
# print a[0:2,1]
# # get array
# list=(1,2,3,4)
# print list
#
# string="nguyen van hung"
# print string[0:2]
# array=[1,2,3,4,5]
# print array

x=np.array([(1,2),(3,4)])
print 'shape of x'
print  x.shape
print x[0,1]
print np.repeat(x,[1,3],1)

data=np.loadtxt('data.txt')
print data

