#code
def RearrangePosNeg(arr,n):
	count = 0
	for i in range(0,n):
		if(arr[i]<0):
			for j in range(i,count,-1):
				arr[j],arr[j-1] = arr[j-1],arr[j]
			count += 1
	

#driver
arr= [-1,12,11,-13,-5,0,6,-7,5,-3,-6]
print(arr)
n = len(arr)
RearrangePosNeg(arr,n)

for i in range(n):
	print(arr[i], end=" ")

