import numpy as np
import pandas as pd
from datetime import datetime
def formate(x):
    return datetime.strptime(x,"%Y %m %d %H")
dataset=pd.read_csv("raw.csv",parse_dates=[["year","month","day","hour"]],index_col=0,date_parser=formate)#读取csv文件内容，并将year,month,day,hour，的数据通过parse_dates传递给date_parser函数，对日期进行转化，并指定index_col=0,索隐列为第0列，转化后的日期作为新的索引列，位于第0列

#print(dataset.columns)
dataset.drop("No",axis=1,inplace=True)#输出“No”这一列
#print(dataset.columns)
dataset.columns=["pollution","dew","temp","press","wnd_dir","wnd_spd","snow","rain"]#重命名每一列的列名
#print(dataset.columns)
dataset.index.name="date"#将索引列重命名为date
dataset["pollution"].fillna(0,inplace=True)#将pollution列中所有na值填充为0，并保持位置
#print(dataset)
dataset=dataset[24:]#删除前24小时的数据,数据是每个小时收集一条，所以删除前24条就删除了前24小时的数据，这样做的木得是消除设备启动时的影响
#print(dataset)
print(dataset.head(5))#打印前5行数据，防止出错

dataset.to_csv("pollution.csv")#将预处理的数据保存到pollution.csv文件中，————————》以上步骤被称为数据清洗


    