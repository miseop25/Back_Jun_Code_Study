import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    tree = list(map(int , input().split(" ")))
    day = N
    tree = sorted(tree)
    for i in range(N) :
        tree[i] -= i
    day += max(tree) + 1
    print(day)