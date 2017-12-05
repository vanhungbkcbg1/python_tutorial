import numpy as np

arran=np.arange(100);
print arran;
a = np.array([
    (1,2),
    (4,5),
    (4,5),
    (4,5)])
print a.shape
# change shape from 3X3 ->
a.reshape(2,4)
print a
print a.ndim
print a[0][0]
print a[0:2,1]
# get array
list=(1,2,3,4)
print list

string="nguyen van hung"
print string[0:2]
array=[1,2,3,4,5]
print array

