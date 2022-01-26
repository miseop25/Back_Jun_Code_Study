T = int(input())

for i in range(T):
    RS = list(input().split())
    
    for j in range(len(RS[1])):
        print(RS[1][j] * int(RS[0]), end = "")
    print()
