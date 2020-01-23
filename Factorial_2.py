def aa(N):
	if N <= 1: 
		return 1
	else :
		return N * aa(N-1)
		
print(aa(5))

##
