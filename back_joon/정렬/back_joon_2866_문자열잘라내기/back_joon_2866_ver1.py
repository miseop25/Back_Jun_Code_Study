import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    answer = 0
    R, C = map(int, input().split(" "))
    word_list = collections.deque(list(collections.deque([]) for i in range(C)))
    first_word = input().rstrip()
    for i in range(1, R) :
        tmep = input().rstrip()
        for j in range(C) :
            word_list[j].append(tmep[j])
    
    for i in range(C -1) :
        w_sets = set()
        j = 0
        for words in word_list :
            w_sets.add("".join(words))
            word_list[j].popleft()
            j += 1
        if len(w_sets) == C :
            answer += 1
        else :
            break
    print(answer)

