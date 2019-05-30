'''
ndarray 객체
numpy를통해생성되는n차원의배열객체
같은종류의데이터만을배열에담을수있음(파이썬리스트는다양한자료저장)
ndarray 인덱싱, 슬라이싱
ndarray 다루기
ndarray 생성–array(), arrange(), zeros(), ones(), linspace(), eye(), random()
ndarray 모양변경–reshape()
ndarray 에서max, min, 값찾기, 연산하기
'''
import numpy as np

print(np.__version__)
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("array : ",arr)
print("array.T : ",arr.T)
print("array.dtype : ",arr.dtype)
print("array.size : ",arr.size)
print("array.itemsize : ",arr.itemsize)
print("array.nbytes : ",arr.nbytes)
print("array.ndim : ",arr.ndim)
print("array.shape : ",arr.shape)

print(arr[2,1], arr[1,2], arr[:,:])

print(arr < 6)


'''============================================'''
A = [1,2,3,4,5]
A2 = []
for x in A:
    A2.append(x * 2)
print(A2)
'''============================================'''
B = np.array(A)
B2 = B*2
print(B2)

print(dir(np.ndarray))

