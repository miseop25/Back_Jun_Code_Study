import sys
input = sys.stdin.readline


def checkEqualLeft(card_list, num, bin_index) :
    answer = []
    while True :
        bin_index = bin_index -1
        if bin_index <0 :
            return answer
        try:
            if card_list[bin_index] == num :
                answer.append(card_list[bin_index])
            else :
                return answer
        except :
            return answer

def checkEqualRight(card_list, num, bin_index) :
    answer = []
    while True :
        bin_index = bin_index +1
        try:
            if card_list[bin_index] == num :
                answer.append(card_list[bin_index])
            else :
                return answer
        except :
            return answer



def checkCard(card_list, num, N) :
    answer = []
    bin_index = N//2
    while True :
        if card_list[bin_index] < num :
            card_list = card_list[bin_index :]
        elif card_list[bin_index] > num :
            card_list = card_list[ : bin_index]
        else :
            answer.append(card_list[bin_index])
            left_answer = len(checkEqualLeft(card_list, num, bin_index))
            right_answer = len(checkEqualRight(card_list, num, bin_index))
            return left_answer + right_answer + 1

        if len(card_list) == 1 :
            return 0 

        bin_index = len(card_list)//2


N = int(input())
card_list = map(int, input().split(" "))
card_list = sorted(card_list)

M = int(input())
find_card_list = map(int, input().split(" "))
final_answer = []
for i in find_card_list :
    ans = checkCard(card_list,i, N)
    final_answer.append(ans)

print(" ".join(map(str, final_answer)))
