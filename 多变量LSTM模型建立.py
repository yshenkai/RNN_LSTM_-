import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM,Dense
from matplotlib import pyplot
def series_to_supervised(data,n_in=1,n_out=1,dropnan=True):
    n_var=1 if type(data) is list else data.shape[1]
    df=pd.DataFrame(data)
    cols,names=list(),list()
    for i in range(n_in,0,-1):
        cols.append(df.shift(i))
        names+=[("var%d(t-%d)"%(j+1,i)) for j in range(n_var)]
    for i in range(0,n_out):
        cols.append(df.shift(-i))
        if i==0:
            names+=[("var%d(t)"%(j+1)) for j in range(n_var)]
        else:
            names+=[("var%d(t+%d)"%(j+1,i)) for j in range(n_var)]
    agg=pd.concat(cols,axis=1)
    agg.columns=names
    if dropnan:
        agg.dropna(inplace=True)
    return agg
            
dataset=pd.read_csv("pollution.csv",header=0,index_col=0)
values=dataset.values
encode=LabelEncoder()#获取标签编码器
#print(values[:,4])
values[:,4]=encode.fit_transform(values[:,4])#对标签进行编码转化
#print(values[:,4])
values=values.astype("float32")
#print(values)

scale=MinMaxScaler(feature_range=(0,1))
scaled=scale.fit_transform(values)
reframe=series_to_supervised(scaled,1,1)
reframe.drop(reframe.columns[[9,10,11,12,13,14,15]],axis=1,inplace=True)


values=reframe.values

num_train_hours=365*24
train=values[:num_train_hours,:]
test=values[num_train_hours:,:]
trainX=train[:,:-1]
trainY=train[:,-1]
testX=test[:,:-1]
testY=test[:,-1]
trainX=trainX.reshape((trainX.shape[0],1,trainX.shape[1]))
testX=testX.reshape((testX.shape[0],1,testX.shape[1]))
print(trainX.shape,trainY.shape,testX.shape,testY.shape)
model=Sequential()
model.add(LSTM(50,batch_input_shape=(None,trainX.shape[1],trainX.shape[2])))
model.add(Dense(1))
model.compile(loss="mae",optimizer="adam")
history=model.fit(trainX,trainY,epochs=50,batch_size=72,validation_data=(testX,testY))
pyplot.plot(history.history["loss"],label="train")
pyplot.plot(history.history["val_loss"],label="test")
pyplot.legend()
pyplot.show()





















