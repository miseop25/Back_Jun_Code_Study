import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    person = list(map(int, input().rstrip().split(" ")))
    person.sort()
    answer = set()
    for i, val in enumerate(person) :
        result = sorted(person, key= lambda x: x%val)
        cnt = 0
        pc = 0
        for x in result :
            if x%val == 0 :
                cnt += val
                pc += 1
            else : break
        if pc >= 2 :
            answer.add(cnt)
    answer = sorted(answer, key= lambda x: -x)
    print(answer[0])

