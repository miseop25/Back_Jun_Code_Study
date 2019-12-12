N = int(input())
answer = 0

house = list(map(int, input().split(' ')))
before_index = house.index(min(house))
answer += house[before_index]

for i in range(1, N) :
    house = list(map(int, input().split(' ')))
    present_index = house.index(min(house))
    
    if before_index == present_index :
        num = [0,1,2]
        del num[present_index]
        if house[num[0]] < house[num[1]] :
            answer += house[num[0]]
            before_index = num[0]
        else :
            before_index = num[1]
            answer += house[num[1]]
    else :
        before_index = present_index
        answer += house[present_index]

print(answer)



