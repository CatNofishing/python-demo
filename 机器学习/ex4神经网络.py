import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.optimize as opt
from sklearn.metrics import classification_report
import time
e=1e-16

def plot_100_images(x):
    index=np.random.choice(5000,100)
    images=x[index]
    fig,ax_array=plt.subplots(10,10,sharex=True,sharey=True,figsize=(8,8))
    for i in range(10):
        for j in range(10):
            ax_array[i,j].matshow(images[i*10+j].reshape(20,20),cmap='gray_r')
    plt.xticks([])
    plt.yticks([])
    plt.show()


def load_mat(path):
    data=loadmat(path)
    x=data['X']
    y=data['y'].flatten()
    return x,y


def expand_y(y):
    result=[]
    for i in y:
        y_array=np.zeros(10)
        y_array[i-1]=1
        result.append(y_array)
    return np.array(result)

def load_weight(path):
    data=loadmat(path)
    return data['Theta1'],data['Theta2']

def serialize(a,b):
    return np.r_[a.flatten(),b.flatten()]

def deserialize(seq):
    return seq[:25*401].reshape(25,401),seq[25*401:].reshape(10,26)

def sigmoid(z):
    return 1/(1+np.exp(-z))

def feed_forwrd(theta,x):
    t1,t2=deserialize(theta)
    a1=x
    z2=a1 @ t1.T
    a2=np.insert(sigmoid(z2),0,1,axis=1)
    z3=a2 @ t2.T
    a3=sigmoid(z3)
    return a1,z2,a2,z3,a3

def cost(theta,x,y):
    a1,z2,a2,z3,a3=feed_forwrd(theta,x)
    first=-y*np.log(a3+e)
    second=(1-y)*np.log(1-a3+e)
    cost=np.sum(first-second)/len(x)
    return cost

def regularized_cost(theta,x,y,l=1):
    t1,t2=deserialize(theta)
    reg=np.sum(t1[:,1:]**2)+np.sum(t2[:,1:]**2)
    return 1/(2*len(x))*reg+cost(theta,x,y)

def sigmoid_gradient(z):
    return sigmoid(z) * (1 - sigmoid(z))

def gradient(theta,x,y):
    t1,t2=deserialize(theta)
    a1,z2,a2,z3,h=feed_forwrd(theta,x)
    d3=h-y
    d2=d3@t2[:,1:]*sigmoid_gradient(z2)
    D2=d3.T@a2
    D1=d2.T@a1
    D=(1/len(x))*serialize(D1,D2)
    return D

def regularized_gradient(theta,x,y,l=1):
    a1,z2,a2,z3,h=feed_forwrd(theta,x)
    D1,D2=deserialize(gradient(theta,x,y))
    t1, t2 = deserialize(theta)
    t1[:,0]=0
    t2[:,0]=0
    reg_D1=D1+(l/len(x))*t1
    reg_D2=D2+(l/len(x))*t2
    return serialize(reg_D1,reg_D2)


def random_init(size):
    return np.random.uniform(-0.12,0.12,size)


def nn_traning(x,y):
    np.random.seed(10)
    init_theta=random_init(10285)
    res=opt.minimize(fun=cost,x0=init_theta,args=(x,y),method='TNC',jac=gradient,options={'maxiter': 400})
    return res

def accuracy(theta, X, y):
    _, _, _, _, h = feed_forwrd(theta, X)
    y_pred = np.argmax(h, axis=1) + 1
    print(classification_report(y, y_pred))


if __name__=='__main__':

    start=time.perf_counter()
    x,raw_y=load_mat('./数据/ex4data1.mat')
    plot_100_images(x)

    x=np.insert(x,0,1,axis=1)
    y=expand_y(raw_y)
    res=nn_traning(x,y)
    print(res)
    accuracy(res.x,x,raw_y)
    end=time.perf_counter()
    print('本次用时{}s'.format(-start+end))
print()
