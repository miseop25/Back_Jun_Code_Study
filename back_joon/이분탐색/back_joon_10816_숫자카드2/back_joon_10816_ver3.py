import sys
import bisect
input = sys.stdin.readline

def checkCard(card_list, num, N) :
    bin_index = bisect.bisect_right(card_list,num)
    if card_list[bin_index-1] == num :
        left = bisect.bisect_left(card_list,num)
        ans = bin_index - left
        return ans
    else :
        return 0

N = int(input())
card_list = map(int, input().split(" "))
card_list = sorted(card_list)

M = int(input())
find_card_list = list(map(int, input().split(" ")))
final_answer = []

pre_card = find_card_list[0]
ans = checkCard(card_list,pre_card, N)
final_answer.append(ans)

for i in find_card_list[1:] :
    if pre_card == i :
        final_answer.append(ans)
    else :
        ans = checkCard(card_list,i, N)
        final_answer.append(ans)
    pre_card = i

print(" ".join(map(str, final_answer)))
