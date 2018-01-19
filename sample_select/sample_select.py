#-*-coding:utf-8-*-
from os import walk
from xml.etree import ElementTree
import random

from os import walk
from jieba import cut

root = ''

file_label = open(root + "label.txt")
file_plus = open(root + "plus.txt")
file_number = open(root + "number.txt")
# root2 = './Marking Result/'

label = file_label.readlines()
# decode()的作用是：将使用其他编码形式的字符转化为Unicode形式，"gbk"是一种常用的编码汉字的编码方式
content = [s.decode('gbk') for s in file_plus.readlines()]
numbers = [int(num) for num in file_number.readlines()]


""" HZP使用人工标记的样本（让学生手动将.xml录入.txt）
part = []
symp = []
for num in numbers:
    path = root2 + str(num / 100) #path为"e:\Marketing\"num/100" "
    #walk()用来遍历文件，os.walk(path)返回的对象是一个3元 tuple : (dir_path,dir_name,file_name)
    for (p, dn, fn) in walk(path):
        for filename in fn:
            #对part文件夹里名字以“n.xxx”开头的文件进行读取
            if filename.startswith(str(num) + '.') and p.endswith("part"):
                symps = open(p + "\\" +  filename.decode("gbk")).readlines()
                part.append(symps)
            #对symptom文件夹里以“n.xxx”开头的文件进行读取
            if filename.startswith(str(num) + '.') and p.endswith("symptom"):
                symps = open(p + "\\" +  filename.decode("gbk")).readlines()
                symp_temp = []
                for s in symps:
                    ss = s.split('\t')
                    for temp_symp in ss:
                        symp_temp.append(temp_symp)
                try:
                    symp.append([w.decode("utf-8") for w in symp_temp])
                except:
                    symp.append([w.decode("gbk") for w in symp_temp])
"""

#最后part里是所有.part文件内容以tab为分隔的集合，symp里是所有.sympton文件。。。。54-94为测试代码，无用

texts_tokenized = []
stopword_list = [',','.',':',';',"'",'"','\\','/','，','？','。','：','《','》','(',')',' ','、','[',']','+','-','*','＋','－','<','>','?','（','）','＇','＂']
stopword = [w.decode('utf-8') for w in stopword_list]
for document in content:
    texts_tokenized_tmp = [w for w in cut(document) if not w in stopword]
    texts_tokenized.append(texts_tokenized_tmp)


from gensim import models, corpora, similarities
import logging
import KNN;
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
'''
dictionary = corpora.Dictionary(symp)
corpus = [dictionary.doc2bow(text) for text in symp]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
num_topic = 10
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic)
lsi_vec = lsi[corpus]
len_dic = len(dictionary)

import KNN

print "LSI with " + str(num_topic) + " topics:"

# ---- lsi_vec(vector) -> vectors(matrix)
vectors = []
for j in range(len(lsi_vec)):
    vectors.append([])
    for i in range(num_topic):
        vectors[j].append(0)
    for w in lsi_vec[j]:
        vectors[j][w[0]] = w[1]

KNN.knn(vectors,label,10)
KNN.knn(vectors,label,10, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])

vectors = []
for j in range(len(corpus_tfidf)):
    vectors.append([])
    for i in range(len_dic):
        vectors[j].append(0)
    for w in corpus_tfidf[j]:
        vectors[j][w[0]] = w[1]

print "Original TF-iDF:"
KNN.knn(vectors,label,10)


---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
dictionary = corpora.Dictionary(texts_tokenized)
corpus = [dictionary.doc2bow(text) for text in texts_tokenized]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
num_topic = 10
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic)
lsi_vec = lsi[corpus]
len_dic = len(dictionary)


print "LSI with " + str(num_topic) + " topics:"

vectors = []
for j in range(len(lsi_vec)):
    vectors.append([])
    for i in range(num_topic):
        vectors[j].append(0)
    for w in lsi_vec[j]:
        vectors[j][w[0]] = w[1]

print '---- K = 10 ----'
KNN.knn(vectors,label,10)
KNN.knn(vectors,label,10, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])
print 
print '---- K = 9 ----'
KNN.knn(vectors,label,9)
KNN.knn(vectors,label,9, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])
print 
print '---- K = 8 ----'
KNN.knn(vectors,label,8)
KNN.knn(vectors,label,8, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])
print 
print '---- K = 7 ----'
KNN.knn(vectors,label,7)
KNN.knn(vectors,label,7, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])
print 
print '---- K = 6 ----'
KNN.knn(vectors,label,6)
KNN.knn(vectors,label,6, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])
print
print '---- K = 5 ----' 
KNN.knn(vectors,label,5)
KNN.knn(vectors,label,5, 1 / similarities.MatrixSimilarity(lsi[corpus])[lsi_vec])
print 

vectors = []
for j in range(len(corpus_tfidf)):
    vectors.append([])
    for i in range(len_dic):
        vectors[j].append(0)
    for w in corpus_tfidf[j]:
        vectors[j][w[0]] = w[1]


print "Original TF-iDF:"
KNN.knn(vectors,label,10)


'''
name = walk("e:\\Marking result\\")
iter = 0
sample = []
samplenumber = []
for root, dirs, files in name:
    if len(str(root)) < 22:
        for fn in files:
            str_fn = str(fn)
            print str_fn
            str_fn = str_fn.split('.')
            sample.append(str_fn[1])
            samplenumber.append(str_fn[0])
            iter = iter + 1
print iter

diag = []
checkup = []
for samp in sample:
    samplename = "e:\\EMRs\\" + samp + ".xml"
    samplename = samplename.decode("gbk")
    root = ElementTree.parse(samplename)
    nod = root.getiterator("inDiag")
    nod2 = root.getiterator("checkUp")
    diag.append(nod[0].text)
    checkup.append(nod2[0].text)

count = 0
out = "e:\\sample2\\"
file_out = open(out + "plus.txt", 'w')
file_no = open(out + "number.txt",'w')
file_label = open(out + "label.txt",'w')
exist = [0 for i in range(1000)]
for i in range(len(diag)):
    if diag[i].find('腰椎间盘脱出'.decode('utf-8')) >= 0:
        print i,diag[i],samplenumber[i]
        print checkup[i]
        subroot = i / 100
        root = "e:\\Marking result\\" + str(subroot) + "\\"
        print root
        count = count + 1
        file_out.write(checkup[i].encode('gbk'))
        file_out.write('\n')
        file_no.write(str(i) + '\n')
        file_label.write('1\n')
        exist[i] = 1
print count
count = 0
while count < 200:
    while True:
        k = random.randint(0,999)
        if exist[k] == 0:
            exist[k] = 1
            break
    print k,diag[k],samplenumber[k]
    print checkup[k]
    subroot = k / 100
    root = "e:\\Marking result\\" + str(subroot) + "\\"
    print root
    file_out.write(checkup[k].encode('gbk'))
    file_out.write('\n')
    file_no.write(str(k) + '\n')
    file_label.write('0\n')
    count = count + 1
'''