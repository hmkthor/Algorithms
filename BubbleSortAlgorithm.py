import random
import time

compare_counter=0
swap_counter=0

def bubble_sort(random_list):
    global compare_counter, swap_counter
    for index in range(len(random_list)-1):
        for start_idx in range(1, len(random_list)-index):
            compare_counter+=1
            if random_list[start_idx-1]>random_list[start_idx]:
                temp=random_list[start_idx-1]
                random_list[start_idx-1]=random_list[start_idx]
                random_list[start_idx]=temp
                swap_counter+=1

if __name__=="__main__":
    list=[]
    input_n = input("how many data do you want to put?")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))
    print("<정렬 전>")
    print(list)

    start_time=time.time()
    bubble_sort(list)
    running_time=time.time()-start_time

    print("<정렬 후>")
    print(list)

    print("데이터의 크기: {}".format(int(input_n)))
    print("비교 횟수 : {}".format(compare_counter))
    print("스왑 횟수 : {}".format(swap_counter))
    print("실행 시간 : {}".format(running_time))

    
