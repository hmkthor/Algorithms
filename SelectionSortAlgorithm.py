# 선택 정렬 알고리즘 

import random
import time

compare_counter = 0
swap_counter = 0

def selected_sort(random_list):
	global compare_counter, swap_counter
	for sel in range(len(random_list)-1):
		min = random_list[sel]
		minindex = sel
		
		for step in range(sel+1, len(random_list)):
			compare_counter+=1
			if min > random_list[step]:
				min = random_list[step]
				minindex = step
				swap_counter+=1
			
		#swap
		random_list[minindex] = random_list[sel] 
		random_list[sel] = min	
			
if __name__=="__main__":
	list = []
	input_n = input("정렬할 데이터의 수 : ")
	for i in range(int(input_n)):
		list.append(random.randint(1, int(input_n)))
	
	print("<정렬전>")
	print(list)
	
	start_time = time.time()
	selected_sort(list)
	running_time=time.time() - start_time
	
	print("<정렬후>")
	print(list)
	
	print("데이터의 크기 : {}".format(int(input_n)))
	print("비교 횟수 : {}".format(compare_counter))
	print("교환 횟수 : {}".format(swap_counter))
	print("실행 시간 : {}".format(running_time))

