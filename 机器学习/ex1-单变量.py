import csv
import numpy as np
import matplotlib.pyplot as plt
file_path=r'数据\ex1data1.txt'
plt.ion()
data=[]
with open(file_path,'r',encoding='utf8') as f:
    reader=csv.reader(f)
    for i in reader:
        x=float(i[0])
        y=float(i[1])
        data.append([x,y])

data=np.array(data)
x=np.array(data[...,0])
size=len(x)
x=x.reshape(size,1)
x=np.insert(x,0,1,axis=1)
y=np.array(data[...,1])
alpha=0.01
num=1500
theta=np.zeros(2)
xlabel=[]
ylabel=[]

for i in range(num):
    temp=theta
    theta[0]=theta[0]-alpha/size*np.sum(np.dot(x,temp)-y)
    theta[1]=theta[1]-alpha/size*np.sum((np.dot(x,temp)-y)*x[...,1])
 
    price=np.sum(np.power((np.dot(x,theta)-y),2))
    xlabel.append(i)
    ylabel.append(price)
    plt.plot(xlabel,ylabel)
    plt.pause(0.000000001)
  
print(theta)

