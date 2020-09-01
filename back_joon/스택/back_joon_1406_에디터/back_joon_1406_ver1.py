import sys
input = sys.stdin.readline

if __name__ == "__main__":
    first = list(input().rstrip())
    last = []
    n = int(input())
    for _ in range(n) :
        cmd = list(input().rstrip().split(" "))
        if cmd[0] == "P" :
            first.append(cmd[1])
        elif cmd[0] == "L" :
            if first :
                temp = first.pop()
                last.append(temp)
        elif cmd[0] == "B" :
            if first :
                first.pop()
        elif cmd[0] == "D" :
            if last :
                temp = last.pop()
                first.append(temp)
    
    last = last[::-1]
    answer = "".join(first) + "".join(last)
    print(answer)

    