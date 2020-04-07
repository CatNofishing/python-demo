from matplotlib import pyplot as plt
import numpy  as np
import matplotlib.ticker as ticker
import pandas as pd
import scipy.optimize as opt


def predict_fun(theta,x):
    return np.dot(x,theta)

def sigmoid(theta,x):
    z=predict_fun(theta,x)
    return 1/(1+np.exp(-1*z))

def cost(theta,x,y):
    first=np.dot(y,np.log(sigmoid(theta,x)))
    second=np.dot((1-y),np.log(1-sigmoid(theta,x)))
    return -np.sum(first+second)/len(x)

def gradient(theta,x,y):
    return 1/len(x)*np.dot(x.T,sigmoid(theta,x)-y)

if __name__=='__main__':
    df=pd.read_csv('./数据/ex2data1.txt',names=['x1','x2','y'])
    df.insert(0,'ones',1)
    x=np.array(df.iloc[:,[0,1,2]])
    y=np.array(df.iloc[:,-1])

    theta=opt.minimize(cost,x0=np.zeros(3),args=(x,y),method='Newton-CG',jac=gradient)
    theta=theta.x
    print(theta)
    print(cost(theta,x,y))
    plt.scatter(x[:,1],x[:,2],c=y)
    plt.plot(x[:,1],(-theta[0]-theta[1]*x[:,1])/theta[2])
    plt.show()