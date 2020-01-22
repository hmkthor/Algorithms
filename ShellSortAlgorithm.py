import random
import time

# 셸 정렬 알고리즘은 선택, 삽입, 버블 알고리즘에 비해 엄청나게 좋은 성능을 보여준다. 
# 선택, 삽입, 버블 정렬 알고리즘들이 데이터 하나를 다른 데이터들과 비교하고, 필요에 따라 이동하는 방식을 기본적으로 
# 사용하기 때문에 결국 O(N^2)의 성능에서 벗어나기 어려운 반면에, 셸 정렬 알고리즘은 하나의 데이터와 
# 그룹간에 비교 이동을 몇 개의 단계로 나누어서 진행하므로 O(N(log2N)) 정도의 성능을 보여준다. 

def shell_sort(random_list):
    h=1
    while h<len(random_list):
        h=3*h+1
    h = h//3

    while h>0:
        for i in range(h):
            start_index = i+h
           

            while start_index < len(random_list):
                temp = random_list[start_index]
                insert_index = start_index

                while insert_index > h-1 and random_list[insert_index-h] > temp:
                    random_list[insert_index] = random_list[insert_index-h]
                    insert_index = insert_index - h
                    

                random_list[insert_index] = temp
                start_index = insert_index + h

        h=h//3

if __name__=='__main__':
    list=[]
    input_n = input("정렬할 데이터의 수 : ")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))
    print("<정렬전>")
    print(list)
    start_time = time.time()
    shell_sort(list)
    running_time = time.time() - start_time
    print("<정렬후>")
    print(list)

    print("데이터 크기 : {}".format(int(input_n)))
    print("실행시간 : {}".format(running_time))