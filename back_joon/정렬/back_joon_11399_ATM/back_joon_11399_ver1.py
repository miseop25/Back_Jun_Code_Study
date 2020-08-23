import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input().rstrip())
    person = list(map(int, input().split(" ")))
    person = sorted(person)
    answer = 0 
    result = []
    for i in person :
        answer = answer + i
        result.append(answer)
    print(sum(result))