N = int(input())
answer = 0
num_str = input()

for i in range(0,N) :
    answer += int(num_str[i])

print(answer)