import sys

for i in range(5):
    # \n included
    #a = sys.stdin.readline() 

    # \n excluded (the rightmost \n will be gone.)
    a = sys.stdin.readline().rstrip()
    print(a)


