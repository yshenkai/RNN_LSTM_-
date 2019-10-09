import pandas as pd
from matplotlib import pyplot
dataset=pd.read_csv("pollution.csv",header=0,index_col=0)#读入csv文件，行0为头部（标题）,索引为第0列
#print(dataset.head(10))
values=dataset.values#获取dateset中的值，返回一个二维矩阵
#print(values)

#下面开始对每一列数据进行绘图，以便观察其变化趋势
groups=[0,1,2,3,4,5,6,7]
i=1
pyplot.figure()#初始化一个画布空间

for group in groups:
    pyplot.subplot(8,1,i)
    pyplot.plot(values[:,group])
    pyplot.title(dataset.columns[group],y=0.5,loc="right")
    i+=1
pyplot.show()


