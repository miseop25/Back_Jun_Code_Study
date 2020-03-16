import itertools

def is_Prime_number(temp) :
    if temp <2 :
        return False
    else :
        for i in range(2, temp) :
            if temp%i == 0 :
                return False
    return True


def solution(numbers):
    num = []
    all_num_list = []
    answer = 0
    for i in range(len(numbers)) :
        num.append(numbers[i])

    for i in range(1, len(numbers)+1) :
        buf = list(map(''.join, itertools.permutations(num,i)))
        buf = map(int, buf)
        all_num_list.extend(buf)
    all_num_list = set(all_num_list)
    for i in all_num_list :
        if is_Prime_number(int(i)) :
            answer  += 1
    
    return answer

print(solution("17"))