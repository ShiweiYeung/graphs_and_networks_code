import numpy as np
from random import choice
from random import sample
import time
start=time.clock()
num_vertex=7#数字总数，一个数字是一个点的编号
num_blocks=0#已经添加进集合B的元素个数
v=set()#点集合
B=set()#存放三元组的集合
v_block=set()#非live point点集
vertex_blocks=np.zeros([num_vertex,1])#每个点出现在B中的次数
for i in range(num_vertex):
    v.add(i)

while num_blocks<num_vertex*(num_vertex-1)/6:
    temp_vertex=choice(list(v-v_block))#从live point中随机选点v
    temp_v=v.copy()#点temp_vertex的所有点对
    temp_v.discard(temp_vertex)#在点对中删去temp_vertex本身
    for b in B:
        if temp_vertex in b:
            for b_element in b:
                temp_v.discard(b_element)#删去在B中的temp_vertex的点对
    # length = len(temp_v)
    temp_edge=sample(list(temp_v),2)#随机取两个点，与temp_vertex组成三元组
    temp_edge0=temp_edge[0]
    temp_edge1 = temp_edge[1]
    indicate=0
    for b in B:
        if (temp_edge0 in b) and (temp_edge1 in b):#若两个点组成的点对在B中，置换，集合B未增大
            list_b=list(b)
            list_b.remove(temp_edge0)
            list_b.remove(temp_edge1)
            temp=list_b[0]
            # temp=(b-temp_edge0)-temp_edge1
            if temp in v_block:
                v_block.discard(temp)
                # num_vertex-=1
                B.remove(b)
                B.add((temp_vertex,temp_edge0,temp_edge1))
                vertex_blocks[temp] = vertex_blocks[temp] - 1#点temp在B中出现次数减1
                vertex_blocks[temp_vertex] = vertex_blocks[temp_vertex] + 1#点temp_vertex在B中出现次数加1

            else:
                B.remove(b)
                B.add((temp_vertex, temp_edge0, temp_edge1))
                vertex_blocks[temp] = vertex_blocks[temp] - 1
                vertex_blocks[temp_vertex] = vertex_blocks[temp_vertex] + 1

            indicate=1
            break
    if not indicate :#若两个点组成的点对不在在B中，添加一个三元组到B，集合B增大
        B.add((temp_vertex, temp_edge0, temp_edge1))
        num_blocks += 1
        vertex_blocks[temp_vertex] = vertex_blocks[temp_vertex] + 1
        vertex_blocks[temp_edge[0]] = vertex_blocks[temp_edge[0]] + 1
        vertex_blocks[temp_edge[1]] = vertex_blocks[temp_edge[1]] + 1
        # if length==2:
        #     num_blocks+=1
        #     v_block.add(temp_vertex)
#若有点在B中的出现次数达到(num_vertex-1)/2，意味着这个点是非live point点，把它加入v_block中
    if vertex_blocks[temp_vertex] ==(num_vertex-1)/2:
        v_block.add(temp_vertex)
        # num_blocks += 1
    if vertex_blocks[temp_edge[0]] ==(num_vertex-1)/2:
        v_block.add(temp_edge[0])
        # num_blocks += 1
    if vertex_blocks[temp_edge[1]] ==(num_vertex-1)/2:
        v_block.add(temp_edge[1])
        # num_blocks += 1
end=time.clock()
print("running time:", end-start)
# print(B)

                
                
                
            

