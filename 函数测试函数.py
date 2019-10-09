import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix#混淆矩阵
y_true=[1,1,1,1,1,1]
y_pred=[0,0,0,0,0,0]
c=confusion_matrix(y_true,y_pred)
print(c)
'''
lb=LabelEncoder()
lb.fit([1,2,3,4,5])
print(lb.classes_)#标签值标准化
print(lb.transform([3,2,1]))
'''

'''
df=pd.DataFrame()
df['t']=[x for x in range(10)]
print(df)
df['t-1']=df['t'].shift(1)
df['t+1']=df['t'].shift(-1)
print(df)
'''