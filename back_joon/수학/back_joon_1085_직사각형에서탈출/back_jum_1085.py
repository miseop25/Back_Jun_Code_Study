x,y,w,h = input().split(' ')

case = []

case.append(int(x))
case.append(int(y))
case.append(int(w)-int(x))
case.append(int(h)-int(y))

answer = min(case)

print(answer)

