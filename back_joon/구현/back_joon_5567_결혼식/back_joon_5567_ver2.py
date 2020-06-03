import sys
input = sys.stdin.readline




if __name__ == "__main__":
    N = int(input())
    m = int(input())
    friend = dict()

    for i in range(1, N+1) :
        friend[i] = []
    
    for _ in range(m) :
        a, b = map(int, input().split(" "))
        friend[a].append(b)
        friend[b].append(a)
    
    ans_set = set(friend[1])
    for i in friend[1] :
        ans_set.update(friend[i])
    print(len(ans_set) - 1)

