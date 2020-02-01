"""
세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면 
A × B × C = 150 × 266 × 427 = 17037300 이 되고, 
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 같거나 크고, 1,000보다 작은 자연수이다.
"""

if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())

    sum = A * B * C 
    list=[]

    for i in range(10):
        list.append(0)

    st = str(sum)
    for i in range(len(st)):
        list[int(st[i])] += 1
    
    for i in range(len(list)):
        print(list[i])
