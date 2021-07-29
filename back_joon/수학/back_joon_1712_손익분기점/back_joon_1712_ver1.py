def soluction() :
    a, b, c = map(int, (input().split(" ")))
    if b >= c :
        return -1 
    value = c - b 
    return (a//value) + 1

print(soluction())


