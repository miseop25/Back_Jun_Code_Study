if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T) :
        x1, x2 = map(str, input().split(" "))
        a = int("0b" + x1, 2)
        b = int("0b" + x2, 2)
        c = a + b
        result = bin(c)
        print(result[2:])


