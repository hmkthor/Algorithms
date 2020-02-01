"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

import sys

if __name__ == '__main__':
    string = sys.stdin.readline().rstrip().split()
    val1 = int(string[0])
    val2 = int(string[1])

    if val1>val2:
        pivot = val2
    else:
        pivot = val1

    #gcd lcm
    for i in range(pivot,0,-1):
        if val1%i==0 and val2%i==0:
            gcd = i
            break
    
    lcm = gcd * (val1//gcd) * (val2//gcd)

    print(gcd)
    print(lcm)