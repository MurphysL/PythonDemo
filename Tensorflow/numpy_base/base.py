import numpy as np

#属性
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print("array_ndim:", array.ndim)
print("array_shape:", array.shape)
print("array_size", array.size)

#创建
a = np.array([[1, 2], [3, 4]], np.float32)
print(a.dtype)
zero = np.zeros((2, 2))
print(zero)
one = np.ones((1, 2))
print(one)
empty = np.empty((2, 1))
print(empty)
arange1 = np.arange(5)
print(arange1)
arange = np.arange(1, 12, 2).reshape((2, 3))
print(arange)
line = np.linspace(1, 10, 10)
print(line)
line2 = np.linspace(1, 10, 10).reshape((2, 5))
print(line2)

line3 = np.linspace(1, 10, 10)[:, np.newaxis]
print(line3)

#运算
x1 = np.array([0, 1, 2, 3])
x2 = np.array([10, 9, 8, 7])
add = x1+x2
print(add)
mul = x1*x2
print(mul)
print(100*np.sin(x1))
print(x1<2)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[1, 0], [0, 1]])
print(np.dot(m1, m2))

x = np.array([0, 1, 2, 3])[:, np.newaxis]
y = np.array([[0, 1, 3]])
bias = np.array([1, 1, 1])
print(x.dot(y)+bias)