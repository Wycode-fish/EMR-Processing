#-*-coding:utf-8-*-
import numpy
from numpy import array
from numpy import append

#这是K=5的KNN算法
def knn(vectors, labels, K=5, sim = []):
    
	n = len(vectors)#矩阵行数
	
	if sim == []:
		#初始化distance矩阵(nxn全零矩阵)
		distance = []
		for i in range(n):
			distance.append([])
			for j in range(n):
				distance[i].append(0)
        #为distance矩阵赋值
		for i in range(n):
			for j in range(i,n):
                #distance中的(i,j)项为“vectors向量的第i项和第j项间的距离”，该矩阵的转制与矩阵本身相等
				distance[i][j] = dis(vectors[i], vectors[j])
				distance[j][i] = distance[i][j]
		for i in range(n):
            #distance[i]为distance的第i行
			distance[i] = array(distance[i])
	else:
		distance = sim

	testindex = [[],[],[],[]]
	for i in range(n/4):
		testindex[0].append(4*i)#[0,4,8,...]，1st of 4-fold cross validation
		testindex[1].append(4*i+1)#[1,5,9,...]，2nd of 4-fold cross validation
		testindex[2].append(4*i+2)#[2,6,10,...]，3rd of...
		testindex[3].append(4*i+3)#[3,7,11,...]，4th of...
        #这个时候testindex矩阵成了一个4x(n/4)的int型矩阵

	indextrain = []
    #[1,2,3,,5,6,7,,9,10,11,...]
	indextrain.append([w for w in range(n) if not w in testindex[0]])
    #[0,,2,3,4,,6,7,8,...]
	indextrain.append([w for w in range(n) if not w in testindex[1]])
    #[0,1,,3,4,5,,7,8,9,,...]
	indextrain.append([w for w in range(n) if not w in testindex[2]])
    #[0,1,2,,4,5,6,,8,9,10,,...]
	indextrain.append([w for w in range(n) if not w in testindex[3]])
    #indextrain成了一个4x(3n/4)的int型矩阵

	av = []
	for t in range(4):
		correct = 0
		for index in testindex[t]:
            #distvec = [dis(0,1),dis(0,2),dis(0,3),dis(0,5),...],(n/4)x(3n/4)
			distvec = [distance[index][j] for j in indextrain[t]]
            #将distvec向量中项按从小到大顺序排列
			sorted_index = numpy.argsort(distvec)
			lb = 0

			for k in range(1,K+1):
                #labels[dis(0,1)],labels[dis(0,2)],...3,...5,...labels[dis(0,n)]中最小的
				lb = lb + int(labels[sorted_index[k]])
			if lb > K/2:
				lb = 1
			else:
				lb = 0
			if lb == int(labels[index]):#labels[0]
				correct = correct + 1
		correct = 1.0*correct/n*4
		av.append(correct);
	av_num = 0;
	for i in range(len(av)):
		av_num = av_num + av[i];
	print "average:",av_num/4;

#计算向量间距离
def dis(vecA, vecB):
    A = array(vecA)
    B = array(vecB)
    dis = numpy.abs(A-B)
    dis = numpy.sqrt(numpy.sum(dis * dis))
    return dis