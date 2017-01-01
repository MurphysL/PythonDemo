import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def logistic(a, b , x):
    return a*x+b
    
def fit(p , x):
    f = np.poly1d(p)
    return f(x)

def residuals(p , x , y):
    return y-fit(p , x)
    

A, B = 2,3
#样本
x0 = np.linspace(0, 10 ,10)
y0 = [np.random.normal(0,1.5) + x for x in logistic(A, B, x0)]
#总体
x1 = np.linspace(0,10,100)

plsq = leastsq(residuals , np.random.randn(3) , (x0 , y0))

plt.plot(x0 , y0 , 'bo')
plt.plot(x0 , fit(plsq[0] , x0))
plt.show()

regularization = 0.0001  # 正则化系数lambda  

#目标函数
def logistic(x):
    return np.sin(2*np.pi * x)

def fit(p,x):
    f=np.poly1d(p)
    return f(x)
 
def residuals(p , y ,x):
    ret= fit(p , x)-y
    #将lambda^(1/2)p加在了返回的array的后面
    ret = np.append(ret, np.sqrt(regularization)*p)
    return ret

x=np.linspace(0,1,9)
x0=np.linspace(0,1,1000)

y0=logistic(x)
y1=[np.random.normal(0 , 0.1) + y for y in y0]#添加正态分布噪声

plsq = leastsq(residuals , np.random.randn(9) , args=(y1 , x))

plt.plot(x0 , logistic(x0) , label='real')
plt.plot(x , y1 , 'bo' , label='noise')
plt.plot(x0 , fit(plsq[0] , x0) , label='fit')#plsq[0] 权值
plt.show()

