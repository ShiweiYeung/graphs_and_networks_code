#minimum spanning tree,Prim算法
import numpy as np
MAX_CONST=100#设置一个极大的权重，设置断开的边的权值等于它，那么在选边的时候就不会选到这些边
A=np.array([[0,4,0,0,0,0,0,8,0],[4,0,8,0,0,0,0,0,11],[0,8,0,7,0,4,0,0,2],[0,0,7,0,9,14,0,0,0],[0,0,0,9,0,10,0,0,0],[0,0,4,14,10,0,2,0,0],[0,0,0,0,0,2,0,1,6],[8,0,0,0,0,0,1,0,7],[0,11,2,0,0,0,6,7,0]])
N=A.shape[0]
output=np.zeros([N,N])#最小支撑树的邻接矩阵
vertex_adding=np.arange(N)
index_zero=np.where(A==0)
A[index_zero]=MAX_CONST
# B=A.copy()

min_index=np.where(A == np.amin(A))#先找一个最小边
output[min_index[0][0],min_index[1][0]]=A[min_index[0][0],min_index[1][0]]
output[min_index[1][0],min_index[0][0]]=A[min_index[0][0],min_index[1][0]]
vertex=list([min_index[0][0],min_index[1][0]])#最小支撑树的点集，开始先添加权值最小的边的两个顶点
# B[:,vertex]=MAX_CONST
vertex_adding=np.delete(vertex_adding,[min_index[0][0],min_index[1][0]])#未选入最小支撑树的点集
while len(vertex)<N:
    temp_min=MAX_CONST
    # temp_min_index=list()
    for i in vertex:
        for j in np.nditer(vertex_adding):
            if temp_min>A[i,j]:#找与最小支撑树相连的最小权值的边
                temp_min_index=list([i,j.item()])
                temp_min=A[i,j]
    vertex.append(temp_min_index[1])#添加点到最小支撑树
    output[temp_min_index[0],temp_min_index[1]]=A[temp_min_index[0],temp_min_index[1]]
    output[temp_min_index[1], temp_min_index[0]] = A[temp_min_index[0], temp_min_index[1]]
    vertex_adding = np.delete(vertex_adding, np.where(vertex_adding==temp_min_index[1]))#在待添加点集中删去刚添加的点


# for i in range(N):
#     for j in range(i,N):

