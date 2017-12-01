import matplotlib.pyplot as plt
import numpy as np
points= np.random.randint(0,100,(25,2),np.int32)
ketqua=np.random.randint(0,2,(25,1))
# print  ketqua
red_points=points[ketqua.ravel()==1]
blue_points=points[ketqua.ravel()==0]
plt.scatter(red_points[:,0],red_points[:,1],100,'r','s')
plt.scatter(blue_points[:,0],blue_points[:,1],100,'b','s')
plt.show()
