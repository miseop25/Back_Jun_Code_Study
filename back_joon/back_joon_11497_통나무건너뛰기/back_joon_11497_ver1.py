import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) : 
    num = int(input())
    tree_list = list(map(int, input().split(" ")))
    tree_list = sorted(tree_list)
    print(tree_list)