# 선택 정렬 알고리즘 

import random

def selected_sort(random_list):
	for sel in range(len(random_list)-1):
		min = random_list[sel]
		minindex = sel
		min2 = min
		
		for step in range(sel+1, len(random_list)):
			if min > random_list[step]:
				min = random_list[step]
				minindex = step
			
		#swap
		random_list[minindex] = random_list[sel] 
		random_list[sel] = min	
			
if __name__=="__main__":
	list=[]
	
	for i in range(10):
		list.append(random.randint(1,10))
	
	print("<Before Sort>")
	print(list)
	
	selected_sort(list)
	
	print("<After Sort>")
	print(list)
