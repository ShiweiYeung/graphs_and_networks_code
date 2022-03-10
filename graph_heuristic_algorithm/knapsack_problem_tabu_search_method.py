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

density=np.true_divide(profits,weight)
temp_index=density.argsort()[::-1]
density=density[temp_index]
profits=profits[temp_index]
weight=weight[temp_index]


#穷举搜索法
max_porfits=0
for i in range(2**15):
    sum_weight=0
    sum_porfits=0
    ind=list()
    count=i
    for k in range(15):
        if count%2==1:
            ind.append(k)
            sum_weight=sum_weight+weight[k]
            sum_porfits=sum_porfits+profits[k]
        count=count>>1
    # print(ind)
    if sum_weight<=capacity and sum_porfits>max_porfits:
        final_knapsack=ind
        max_porfits=sum_porfits

# #模拟淬火法
# a=0.999
# T=100000
# T_min=1
# # max_iterations=10000
# select=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# sum_profit=0
# best_profit=sum_profit
# iterations=0
# max_hold_time=1000
# best_select=np.zeros([1,15])
# best_hold_time=0
# neighbor_size=2
# while T>=T_min:
#     current_select=select.copy()
#     for i in range(neighbor_size):
#         random_select = random.randint(0, 14)
#         current_select[random_select] = 1 - current_select[random_select]
#     while 1:
#         if weight.dot(current_select.T)<=capacity:
#             break
#         else:
#             temp_index=np.where(current_select==1)
#             temp_random=random.randint(0,temp_index[0].shape[0]-1)
#             # print(temp_random)
#             current_select[temp_index[0][temp_random]]=0
#     current_profit=profits.dot(current_select.T)
#     if current_profit>sum_profit:
#         sum_profit=current_profit
#         select=current_select.copy()
#         if current_profit>best_profit:
#             best_profit=current_profit
#             best_select=current_select.copy()
#             print(best_select,best_profit)
#             best_hold_time=0
#     else:
#         if random.random()<math.exp((current_profit-sum_profit)/T):
#             sum_profit = current_profit
#             select = current_select.copy()
#     T=T*a
#     iterations+=1
#     best_hold_time+=1
#     if best_hold_time>max_hold_time:
#         print("最优解长期不变，停止")
#         break

# 禁忌搜索法

best_profit=np.zeros([20])
best_iterations=np.zeros([20])
for tabu_length in range(20):
    max_iterations=1000
    # last_select=np.array([1,1,1,1,1,1,1,1,0,1,0,0,0,0,0])
    last_profit=0

    iterations=0
    max_hold_time=1000
    best_select=np.zeros([1,15])
    best_hold_time=0
    neighbor_size=1
    tabu_list=list()
    # tabu_length=20


    current_select=np.array([1,0,1,1,1,1,0,0,0,0,0,0,0,0,1])
    local_profect=tabu_length+5
    while iterations<max_iterations:
        index0=np.where(current_select==0)
        add_indication=0
        for i in range(index0[0].shape[0]):
            if (weight.dot(current_select.T)+weight[index0[0][i]])<=capacity:
                temp=current_select.tolist()
                temp[i]=1
                if not(temp in tabu_list):
                    add_indication=1

                    if local_profect<tabu_length:
                        tabu_list.append(current_select.tolist())
                        local_profect += 1
                        if local_profect == tabu_length:
                            local_profect = tabu_length + 5
                        if len(tabu_list) > tabu_length:
                            tabu_list.pop(0)
                    current_select[index0[0][i]] = 1
                    break
        if not add_indication:
            if local_profect==tabu_length+5:
                local_profect=0
                # tabu_list=list()
            for j in range(weight.shape[0]):
                if current_select[j]==1 and not(j in tabu_list):
                    temp = current_select.tolist()
                    temp[j] = 0
                    if not(temp in tabu_list):
                        tabu_list.append(current_select.tolist())
                        current_select[j]=0
                        # tabu_list.append(temp)
                        local_profect+=1
                        if local_profect==tabu_length:
                            local_profect=tabu_length+5
                        if len(tabu_list)>tabu_length:
                            tabu_list.pop(0)
                        break
        current_profit=profits.dot(current_select.T)
        if current_profit>best_profit[tabu_length]:
            best_profit[tabu_length]=current_profit
            best_select=current_select.copy()
            best_iterations[tabu_length]=iterations

            # print(best_profit,iterations)
        iterations+=1

# pl.figure(1)
# pl.plot(np.arange(20),best_iterations)
# pl.xlabel('禁忌表长度')
# pl.ylabel('达到最优值需要的迭代次数')
# pl.title('禁忌表长度对迭代次数影响')
# pl.figure(2)
# pl.plot(np.arange(20),best_profit)
# pl.xlabel('禁忌表长度')
# pl.ylabel('最优的profit')
# pl.title('禁忌表长度对最优profit影响')






