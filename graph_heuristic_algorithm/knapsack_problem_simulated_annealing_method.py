import numpy as np
import random
import math
import pylab as pl
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题


profits=np.array([135,139,149,150,156,163,173,184,192,201,210,214,221,229,240])
weight=np.array([70,73,77,80,82,87,90,94,98,106,110,113,115,118,120])
capacity=750

# density=np.true_divide(profits,weight)
# temp_index=density.argsort()[::-1]
# density=density[temp_index]
# profits=profits[temp_index]
# weight=weight[temp_index]


#模拟淬火法
ITE=np.zeros(200)
PRO=np.zeros(200)
for i in range(200):
    a=0.999
    T=i*5
    T_min=1
    # max_iterations=10000
    select=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    sum_profit=0
    best_profit=sum_profit
    iterations=0
    max_hold_time=1000
    best_select=np.zeros([1,15])
    best_hold_time=0
    neighbor_size=2
    while T>=T_min:
        current_select=select.copy()
        for i in range(neighbor_size):
            random_select = random.randint(0, 14)
            current_select[random_select] = 1 - current_select[random_select]
        while 1:
            if weight.dot(current_select.T)<=capacity:
                break
            else:
                temp_index=np.where(current_select==1)
                temp_random=random.randint(0,temp_index[0].shape[0]-1)
                # print(temp_random)
                current_select[temp_index[0][temp_random]]=0
        current_profit=profits.dot(current_select.T)
        if current_profit>sum_profit:
            sum_profit=current_profit
            select=current_select.copy()
            if current_profit>best_profit:
                best_profit=current_profit
                best_select=current_select.copy()
                # print(best_select,best_profit)
                best_hold_time=0
        else:
            if random.random()<math.exp((current_profit-sum_profit)/T):
                sum_profit = current_profit
                select = current_select.copy()
        T=T*a
        iterations+=1
        best_hold_time+=1
        if best_hold_time>max_hold_time:
            # print("最优解长期不变，停止")
            break
    ITE[i]=iterations
    PRO[i]=best_profit


