import numpy as np
# B(행,열)
L = [1,3,5,7,9]
A = np.array(L)
print(A)
print(A+2)
print(A*2)
print(A*A)

R = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
B = np.array(R)
print(B)

print(B[2:4,1:3])

T = np.arange(10)
print(T)
T = np.arange(1,10,2)
print(T)

n = np.empty([2,2])
print(n)
n = np.empty([2,2], dtype=int)
print(n)

print(np.linspace(1,2, num=2))
print(np.linspace(1,2))
print(np.linspace(1,5, num=3))
print(np.linspace(1,5, num=4))
print(np.linspace(1,5, num=3, endpoint=False))

L = [1,2,3,4]
A = np.array(L)
B = A
B[2] = 100
print(A, B)

L = [1,2,3,4]
A1 = np.array(L)
B1 = np.copy(A1)
B1[2] = 100
print(A1, B1)

