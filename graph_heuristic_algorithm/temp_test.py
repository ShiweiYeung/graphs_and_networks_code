import math
import numpy as np
import pylab as pl
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

y=np.array([584,1027,571,704])
z=np.array([1455,1450,1446,1454])
t=np.array([9,6,3,0])

x=np.arange(10)
pl.figure(1)
# pl.axes(xscale='log')
pl.plot(t,y)
pl.xlabel('初始值中1 的个数')
pl.ylabel('达到最优解的总迭代次数')
pl.title('初始值中1 的个数对总迭代次数影响')

pl.figure(2)
# pl.axes(xscale='log')
pl.plot(t,z)
pl.xlabel('初始值中1 的个数')
pl.ylabel('最优的profit')
pl.title('初始值中1 的个数对最优的profit影响')