import numpy as np
import random
#使用第二种算法
class MatrixGraph:
    '''
    无向图的邻接矩阵表示(为对称矩阵),对角线全为零，使用顶点编号（vertex,类型为list）初始化图
    vex2num为字典，将顶点映射为矩阵的编号
    '''

    def __init__(self, vertex=[]):
        '''
        根据传入的顶点信息表建造邻接矩阵和顶点字典
        :param vertex：无向图的所有顶点组成的列表
        '''
        self.vexNum = len(vertex)
        self.adjMatrix = np.zeros((self.vexNum, self.vexNum))
        self.vex2num = {}
        for index, vertex in enumerate(vertex):
            self.vex2num[vertex] = index

    def createGraph(self, matrix):
        '''
        传入一个矩阵确立顶点间的关系
        '''
        if matrix.shape == self.adjMatrix.shape:
            self.adjMatrix = matrix.copy()
        else:
            raise Exception('wrong matrix shape')

'''
创建图的随机矩阵，需要指定图的节点数（N）节点的最小度数（MinDegree）和最大度数（MaxDegree）
然后在MinDegree和MaxDegree范围内随机生成每个节点的度数temp_degree，然后在矩阵对应行随机生成temp_degree个1
'''
N=200
MinDegree=15
MaxDegree=18
vexs=[]
for i in range(1,N+1):
    vexs.append(str(i))

matrix=np.zeros((N,N))
CountDegree=np.zeros(N)
CountIndexNumpy=np.arange(N)
t=0
CountIndex=CountIndexNumpy.tolist()
for ii in range(N-1-MaxDegree):
    if MinDegree-CountDegree[ii]>0:
        temp_degree = np.random.randint(MinDegree - CountDegree[ii], MaxDegree - CountDegree[ii], 1)
        temp_degree=int(temp_degree)
        X=CountIndex[ii + 1:N]
        temp_vex=random.sample(X, temp_degree)
        matrix[ii, temp_vex] = 1
        matrix[temp_vex, ii] = 1
        CountDegree = np.sum(matrix, axis=1)
CountDegree=np.sum(matrix,axis=1)

for ii in range(N-1-MaxDegree,N):
    if CountDegree[ii]<MinDegree:

        temp_degree= MinDegree - CountDegree[ii]
        for jj in range(N-1,-1,-1):
            if temp_degree==0:
                break
            if (jj!=ii)and (matrix[ii,jj]==0):
                matrix[ii,jj]=1
                matrix[jj,ii]=1
                temp_degree-=1
                CountDegree[ii]+=1
                CountDegree[jj]+=1
for i in range(N):
    matrix[ii,ii]=1
#检查生成的matrix是不是0-1对称矩阵
for ii in range(N):
    for jj in range(N):
        if matrix[ii,jj]==matrix[jj,ii]:
            continue
        else:
            print("matrix is not symmetrical")
else:
    if ii==N-1 and jj==N-1:
        print("matrix is symmetrical")

print("The degree of each vertex is ",np.sum(matrix,axis=0))
# print(matrix)
# matrix=np.array([[0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
#  [0, 0, 0, 0, 1, 0, 1, 0, 1, 0,],
#  [0, 0, 0, 1, 1, 0, 0, 0, 0, 1,],
#  [0, 0, 1, 0, 1, 0, 0, 1, 0, 1,],
#  [0, 1, 1, 1, 0, 0, 1, 1, 1, 0,],
#  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
#  [0, 1, 0, 0, 1, 0, 0, 0, 0, 1,],
#  [1, 0, 0, 1, 1, 1, 0, 0, 0, 0,],
#  [1, 1, 0, 0, 1, 1, 0, 0, 0, 0,],
#  [1, 0, 1, 1, 0, 1, 1, 0, 0, 0,]])
#由邻接矩阵创建图
Mgraph = MatrixGraph(vexs)
Mgraph.createGraph(matrix)

'''
使用贪心算法取点，每次计算出最小支配点数（temp_min_domainlated_point_num）后，从第一个点按次序遍历，
直到找到一个点的度数大于或等于最小支配点数时，从原图删去此点，并计算剩余未支配的点数（NotDomainlatedNum）
'''
MAX_ITERATION=N #最大迭代次数不会超过N
NotDomainlatedNum=Mgraph.vexNum
tempMatrix=Mgraph.adjMatrix.copy()
recordDomainlatedPoint=np.zeros([N])
for i in range(1,MAX_ITERATION):
    if not (NotDomainlatedNum * (1+MinDegree))%(Mgraph.vexNum):
        temp_min_domainlated_point_num = NotDomainlatedNum * (1+MinDegree) / (Mgraph.vexNum)
    else:
        temp_min_domainlated_point_num=int(NotDomainlatedNum * (1+MinDegree) / (Mgraph.vexNum))+1
    if temp_min_domainlated_point_num==1:
        t=i-1
        for iii in range(N):

            if not recordDomainlatedPoint[iii]:
                print("delete point %d" %(iii))
                temp_index = np.nonzero(Mgraph.adjMatrix[iii, :])
                temp = np.append(temp_index[0], iii).tolist()
                for jjj in temp:
                    if recordDomainlatedPoint[jjj] == 0:
                        recordDomainlatedPoint[jjj] = 1
                        NotDomainlatedNum -= 1
                t+=1
                recordDomainlatedPoint[iii] = 1
        break
    print("temp_min_domainlated_point_num=%d" %(temp_min_domainlated_point_num))
    remain_point_degree=np.sum(matrix,axis=1)
    print("Iteration %d NotDomainlatedNum=%d" % (i, NotDomainlatedNum), end=",")
    if NotDomainlatedNum < 1:
        print("There is no domainlated point")
        break
    temp_id = 0
    for j in range(matrix.shape[0]):
        if remain_point_degree[j]>=temp_min_domainlated_point_num: #找到一个点度数大于temp_min_domainlated_point_num
            temp_id = 1
            temp_index=np.nonzero(Mgraph.adjMatrix[j,:])
            temp = np.append(temp_index[0], j).tolist()
            for jjj in temp:
                if recordDomainlatedPoint[jjj] == 0:
                    recordDomainlatedPoint[jjj] = 1
                    NotDomainlatedNum -= 1
            matrix[temp_index,:]=0 #把与该点连接的点的行的值全改为0，这是与第一种算法的区别
            matrix[j,:]=0#把该点所在行的值全改为0
            matrix[:,j]=0#把该点所在列的值全改为0
            matrix[:,temp_index]=0#把与该点连接的点的列的值全改为0
            print("Delete the point j=%d" %(j))
            break
    if not temp_id:
            print("\n No point has a degree greater than temp_min_domainlated_point_num, error ")
            break
if t==0:
    t=i
print("\n Total number of points is %d" %(t))
# print(recordDomainlatedPoint)

