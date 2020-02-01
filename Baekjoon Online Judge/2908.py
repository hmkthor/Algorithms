"""
상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 
상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734과 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 
따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
"""
import sys

if __name__ == '__main__':
    string = sys.stdin.readline().rstrip().split()
    val1 = int(string[0])
    val2 = int(string[1])

    val1_100 = val1//100
    val1_10 = (val1 - val1_100*100)//10
    val1_1 = val1 - val1_100*100 - val1_10*10

    val2_100 = val2//100
    val2_10 = (val2 - val2_100*100)//10
    val2_1 = val2 - val2_100*100 - val2_10*10

    sangsu_val1 = 100*val1_1 + 10*val1_10 + val1_100
    sangsu_val2 = 100*val2_1 + 10*val2_10 + val2_100

    if sangsu_val1>sangsu_val2:
        print(sangsu_val1)
    else:
        print(sangsu_val2)
