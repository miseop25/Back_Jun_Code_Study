from collections import deque

def soluction(word) :
    st = []
    ed = []
    for i, val in enumerate(word) :
        if i%2 == 1 :
            ed.append(val)
        else : 
            st.append(val)
    result = "".join(st) + "".join(ed[::-1])
    return result


if __name__ == "__main__":
    N = int(input())
    word = input().rstrip()
    cnt = 1
    buf = word
    word = soluction(word)
    N -= 1
    while buf != word and N >= 1 :
        word = soluction(word)
        cnt += 1
        N -= 1
    if N >= 1 :
        for _ in range(N%cnt) :
            word = soluction(word)
    print(word)