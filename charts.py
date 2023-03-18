import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##
# 学习如何绘制图表
# #
def __chart_Spring__():
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    z = np.linspace(0,13,1000)
    x = 5*np.sin(z)
    y = 5*np.cos(z)
    zd = 13*np.random.random(100)
    xd = 5*np.sin(zd)
    yd = 5*np.cos(zd)
    ax1.scatter3D(xd,yd,zd, cmap='Blues')  #绘制散点图
    ax1.plot3D(x,y,z,'gray')    #绘制空间曲线
    plt.show()

def __chart_Pie__():
    print('pie chart')
__chart_Spring__()
__chart_Pie__()