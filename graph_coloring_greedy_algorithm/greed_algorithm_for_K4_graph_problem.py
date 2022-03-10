import numpy as np
#初始化
N=10
graph_matrix=np.zeros([N,N])

#自定义函数1：计算4顶点K4权重
def calculate_weight(matrix,i,j,m,n):
    K4_edge=np.array([matrix[i,j],matrix[i,m],matrix[i,n],matrix[j,m],matrix[j,n],matrix[m,n]])
    K4_edge_no_coler=np.where(K4_edge==0)
    if len(K4_edge_no_coler[0])==0:
        return 0
    K4_edge_white=np.where(K4_edge==1)
    K4_edge_black = np.where(K4_edge == -1)
    if len(K4_edge_white[0]) and len(K4_edge_black[0]):
        return 0
    if (not len(K4_edge_black[0]))and (not len(K4_edge_white[0])):
        return 2**(-5)
    if ((len(K4_edge_white[0]))and (not len(K4_edge_black[0])))or ((not len(K4_edge_white[0]))and (len(K4_edge_black[0]))):
        return 2**(-6+(len(K4_edge_white[0])+len(K4_edge_black[0])))

#自定义函数2：计算一条边所在的四顶点图的K4权重之和，这里还有优化空间
def sum_weight(matrix,i,j):
    output=0
    vertex_index = np.arange(matrix.shape[0])
    for m in np.nditer(np.delete(vertex_index,[i,j])):
        for n in np.nditer(np.delete(vertex_index,[i,j,m])):
            output=output+calculate_weight(matrix,i,j,m,n)
    return output

#自定义函数3：检查生成的邻接矩阵有多少个K4
def calculate_K4_num(matrix):
    output=0
    for i in np.nditer(np.arange(matrix.shape[0]-3)):
        for j in np.nditer(np.arange(i+1,matrix.shape[0]-2)):
            for m in np.nditer(np.arange(j+1,matrix.shape[0]-1)):
                for n in np.nditer(np.arange(m+1,matrix.shape[0])):
                    if matrix[i,j]==matrix[i,m] and matrix[i,j]==matrix[i,n] and matrix[i,j]==matrix[j,m] and matrix[i,j]==matrix[j,n] and matrix[i,j]==matrix[m,n]:
                        output+=1
    return output

for i in range(N):
    for j in range(i+1,N):
        graph_matrix[i,j]=1
        graph_matrix[j,i]=1
        temp_white_weight=sum_weight(graph_matrix,i,j)
        graph_matrix[i, j] =-1
        graph_matrix[j, i] =-1
        temp_black_weight = sum_weight(graph_matrix, i, j)
        if temp_black_weight<=temp_white_weight:
            continue
        else:
            graph_matrix[i, j] = 1
            graph_matrix[j, i] = 1
# print (graph_matrix)
K4_num=calculate_K4_num(graph_matrix)

