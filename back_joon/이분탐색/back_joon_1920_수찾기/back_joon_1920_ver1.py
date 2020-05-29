import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split(" ")))
    num_dict = dict()
    for i in num :
        num_dict[i] = True
    
    M = int(input())
    find_num = list(map(int, input().split(" ")))
    for i in find_num :
        if i in num_dict :
            print(1)
        else :
            print(0)
