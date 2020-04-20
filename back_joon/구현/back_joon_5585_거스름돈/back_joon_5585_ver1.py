import sys
input=sys.stdin.readline

Price = int(input())

change = 1000 - Price
cnt = 0

while change != 0 :
    if change >=500 :
        cnt +=1 
        change = change - 500
    elif change >= 100 :
        cnt += 1
        change = change - 100
    elif change >= 50 :
        cnt += 1
        change = change - 50
    elif change >= 10 :
        cnt += 1
        change = change - 10
    elif change >= 5 :
        cnt += 1
        change = change - 5
    elif change >= 1 :
        cnt += 1
        change = change - 1

print(cnt)

