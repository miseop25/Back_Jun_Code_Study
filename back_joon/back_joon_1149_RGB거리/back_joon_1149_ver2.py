import sys
input = sys.stdin.readline

N = int(input())
answer = 0
color_dict = dict()
first_house = list(map(int, input().split(' ')))
for i in range(3) :
    color_dict[i] = first_house[i]

for _ in range(N-1) :
    outher_house = list(map(int, input().split(' ')))
    red = color_dict[0]
    green = color_dict[1]
    blue = color_dict[2]

    buf = [[],[],[]]
    buf[0].append(green + outher_house[0])
    buf[0].append(blue + outher_house[0])

    buf[1].append(red + outher_house[1])
    buf[1].append(blue + outher_house[1])

    buf[2].append(red + outher_house[2])
    buf[2].append(green + outher_house[2])

    for j in range(3) :
        color_dict[j] = min(buf[j])


print(min(color_dict.values()))


