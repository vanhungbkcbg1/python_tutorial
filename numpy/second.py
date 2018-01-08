import numpy as np

a=np.array([

    (0,1,2,3,4,5),
    (10,11,12,13,14,15),
    (20,21,22,23,24,25),
    (30,31,32,33,34,35),
])

print  a

print a.ravel()

print a[[1,2,3],[3,3,4]]


print a[a%10==0]

b=np.array([
    (True),
    (True),
    (False),
    (True)
])

print 'a'
print a[a%3==0]

print a[b]