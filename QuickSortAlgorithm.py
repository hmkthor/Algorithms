import random
import time

compare_count=0
swap_count=0

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def pivotFirst(x,lmark, rmark):
    pivot = x[lmark]
    pivot_index = lmark
    while lmark <= rmark:
        while lmark<=rmark and x[lmark] <= pivot:
            lmark += 1
        
        while lmark<=rmark and x[rmark] >= pivot:
            rmark -= 1

        if lmark<=rmark:
            swap(x,lmark,rmark)
            lmark += 1
            rmark -= 1
    
    swap(x,pivot_index,rmark)
    return rmark
        

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            pivot = pivotMethod(x, first, last)
            _qsort(x,first,pivot-1)
            _qsort(x,pivot+1,last)
    _qsort(x,0,len(x)-1)


if __name__=="__main__":
    list=[]
    input_n = input("정렬할 데이터의 수")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))
    print("<정렬 전>")
    print(list)

    start_time = time.time()
    quickSort(list)
    running_time = time.time()-start_time

    print("<정렬 후>")
    print(list)

