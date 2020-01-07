fibonacci = [[1,0], [0,1] ]

for i in range(2 , 40) :
    fibonacci.append([])
    fibonacci[i].append(fibonacci[i-1][0] + fibonacci[i-2][0])
    fibonacci[i].append(fibonacci[i-1][1] + fibonacci[i-2][1])


T = int(input())

for _ in range(T) :
    N = int(input())
    print(fibonacci[N][0], fibonacci[N][1])

