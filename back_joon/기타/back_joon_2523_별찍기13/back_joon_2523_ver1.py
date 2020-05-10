N = int(input())

for i in range(1,N+1) :
    star = ""
    for j in range(i) :
        star += "*"
    print(star)
for i in range(N-1, 0, -1) :
    star = ""
    for j in range(i) :
        star += "*"
    print(star)
