import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1,4))
array3 = np.zeros((2,5))

try:
	print(array1[4])  #index error
	print(array1[0][0])  #syntax error
	print(array1[0][0])  #index error
	print(array2[1][0])  #index error
	print(array2[2][0])  #index error
	

except IndexError as e:
	print(f'SORRY hehe T-T')
