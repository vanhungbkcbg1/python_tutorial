from matplotlib import  pyplot as plt
plt.plot([1,2,3],[4,5,1],color='green',linestyle='dashed',marker='o',alpha=0.5)
plt.title('hello')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([0,6,0,10])
plt.show()
