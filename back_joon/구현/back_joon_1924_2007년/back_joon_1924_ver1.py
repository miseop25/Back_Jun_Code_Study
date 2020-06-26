year = {1: 31, 2: 28, 3: 31, 4 : 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day = ["MON", "TUE", "WED", "THU", "FRI","SAT","SUN"]
m, d = map(int, input().split(" "))
totalDay = 0
for i in range(1, m) :
    totalDay += year[i]
totalDay += d -1
print(day[totalDay%7])