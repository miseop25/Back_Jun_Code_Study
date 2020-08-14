import math
import itertools

if __name__ == "__main__":
    num = list(map(int, input().split(" ")))
    result = itertools.combinations(num, 3)
    answer = []
    for i in result :
        lcm = i[0]
        for j in i[1:] :
            lcm = int(lcm*j / math.gcd(lcm, j))
        answer.append(lcm)
    print(min(answer))