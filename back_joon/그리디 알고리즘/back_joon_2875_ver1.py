girl, boy, intern = map(int, input().split(" "))
for _ in range(intern) :
    if girl < boy*2 :
        boy -= 1
    elif girl >= boy*2 :
        girl -= 1

max_team = 0
i = boy
while i >= 0 :
    if i*2 <= girl :
        max_team = i
        break
    else :
        i -= 1
print(max_team)

