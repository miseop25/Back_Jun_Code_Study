def soluction(a,b) :
    a = a[::-1]
    b = b[::-1]
    return max(int(a), int(b))

if __name__ == "__main__":
    a, b = map(str, input().split(" "))
    print(soluction(a,b))
