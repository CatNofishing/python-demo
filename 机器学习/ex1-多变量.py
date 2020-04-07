import csv
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
file_path=r'数据\ex1data2.txt'
data=[]
with open(file_path,'r',encoding='utf8') as f:
    reader=csv.reader(f)
    for i in reader:
        x=float(i[0])
        y=float(i[1])
        z=float(i[2])
        data.append([x,y,z])

data=np.array(data)
x=data[...,0:2]
y=data[...,2]
x_min=np.min(x,axis=0)
x_max=np.max(x,axis=0)
y_max=np.max(x)
y_min=np.min(x)
x=(x-x_min)/(x_max-x_min)
y=(y-y_min)/(y_max-y_min)
x=np.insert(x,0,1,axis=1)
alpha=0.01
m=x.shape[0]
theta=np.zeros(x.shape[1])
num=150000

xlabel=[]
ylabel=[]

for i in range(num):
    temp=theta
    for j in range(x.shape[1]):
        if j==0:
            theta[j]=theta[j]-alpha/m*np.sum(np.dot(x,temp)-y)
        else:
            theta[j]=theta[j]-alpha/m*np.sum((np.dot(x,temp)-y)*x[...,j])
    '''
    price=np.sum(np.power((np.dot(x,theta)-y),2))
    xlabel.append(i)
    ylabel.append(price)
    plt.plot(xlabel,ylabel)
    plt.pause(0.1)
    '''


print('梯度下降法')
print(theta)
print('正规方程法')
theta=np.linalg.inv(np.dot(x.T,x))
theta=np.dot(theta,x.T)
theta=np.dot(theta,y)
print(theta)