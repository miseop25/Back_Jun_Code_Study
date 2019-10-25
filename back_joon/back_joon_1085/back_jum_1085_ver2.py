x,y,w,h = map(int, input().split(' '))

case = [x,y,w-x,h-y]
answer = min(case)

print(answer)

