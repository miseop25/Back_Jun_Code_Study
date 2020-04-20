import sys
input = sys.stdin.readline

N = int(input())
answer = 0
color_dict = dict()
first_house = list(map(int, input().split(' ')))
for i in range(3) :
    color_dict[i] = first_house[i]

for _ in range(N-1) :
    other_house = list(map(int, input().split(' ')))
    red = color_dict[0]
    green = color_dict[1]
    blue = color_dict[2]

    buf = [[],[],[]]

    # red으로 칠할때!
    buf[0].append(green + other_house[0])
    buf[0].append(blue + other_house[0])
    # green으로 칠할때
    buf[1].append(red + other_house[1])
    buf[1].append(blue + other_house[1])
    # blue 로 칠할 때
    buf[2].append(red + other_house[2])
    buf[2].append(green + other_house[2])

    #  최소값 딕셔너리에 다시 저장
    for j in range(3) :
        color_dict[j] = min(buf[j])


print(min(color_dict.values()))


