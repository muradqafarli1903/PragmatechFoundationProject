import numpy as np
arr= np.array([1,2,3,4,5,6,7,8])
size1=int(input('arrayi nece olculu etmek istediyinizi daxil edin: '))
size2=int(input('her arraydeki elemet sayi :'))
print(arr.reshape((size1,size2)))