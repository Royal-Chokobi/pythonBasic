import numpy as np

L = [[11,22,33,44]
     ,[55,66,77,88]
     ,[90,10,30,50]
     ,[70,80,90,20]
     ,[88,77,66,55]]
A = np.array(L)

print(A)
print("1행 : ", A[1,:])
print("1열 : ", A[:,1])

print(A[:,::2])
A[::2,::2] = -5
print(A)
A[1:,1:3] = 0
print(A)

A2 = np.array(L)
A2= A2 *2
print(A2)

print(1/A2)