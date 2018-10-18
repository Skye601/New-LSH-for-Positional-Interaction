import numpy as np
import matplotlib.pyplot as plt
import random as ran



'''
创建自身点
'''
MyX=50
MyY=50
MyPos = [MyX,MyY]

'''
随机创建向量用来描述相对位置。
'''
Ax = ran.uniform(0,100)
Ay = ran.uniform(0,100)
k = Ay / Ax
if (k>1):
    Ay = np.arange(0,100,0.01)
    Ax = np.arange(0,100/k,0.01/k)
else:
    Ay = np.arange(0,100*k,0.01*k)
    Ax = np.arange(0,100,0.01)

'''
计算投影
'''
MyK = -1/k


'''
绘图
'''
plt.scatter(MyX,MyY)
plt.plot(Ax,Ay,'g')

plt.xlim(0,100)
plt.ylim(0,100)
plt.grid(True)
plt.show()