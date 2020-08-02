import sys
input = sys.stdin.readline

def soluction() :
    code = input().rstrip()
    st1 = []
    st2 = []

    for i in code :
        if i == "<" :
            if st1 :
                st2.append(st1.pop())
        elif i == ">" :
            if st2 :
                st1.append(st2.pop())
        elif i == "-" :
            if st1 :
                st1.pop()
        else :
            st1.append(i)
    st2.reverse()
    result = "".join(st1) + "".join(st2)
    return result


if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        print(soluction())