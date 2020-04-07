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

def fun(theta,x,y):
    return theta[0]+theta[1]*x+theta[2]*y+theta[3]*x**2+theta[4]*y**2



if __name__=='__main__':
    df=pd.read_csv('./数据/ex2data2.txt',names=['x1','x2','y'])
    df.insert(0,'ones',1)
    x=np.array(df.iloc[:,[0,1,2]])
    y=np.array(df.iloc[:,-1])
    x1_2=(x[:,1]**2).reshape(len(x),1)
    x2_2=(x[:,2]**2).reshape(len(x),1)
    x=np.concatenate((x,x1_2,x2_2),axis=1)
    theta=opt.minimize(cost,x0=np.zeros(5),args=(x,y),method='Newton-CG',jac=gradient)
    print(theta)
    theta=theta.x

    x_draw=np.linspace(x[:,1].min(),x[:,1].max(),num=1000)
    y_draw=np.linspace(x[:,2].min(),x[:,2].max(),num=1000)
    x_draw,y_draw=np.meshgrid(x_draw,y_draw)

    
    plt.scatter(x[:,1],x[:,2],c=y)
    plt.contour(x_draw,y_draw,fun(theta,x_draw,y_draw),0)
    plt.show()

from PyQt5.QtWidgets import QApplication