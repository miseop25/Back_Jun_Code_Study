import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().rstrip()
    wordList = ["pi", "ka", "chu"]
    l = len(word)
    cnt = 0
    temp = str(word)
    for i in range(3) :
        cnt += word.count(wordList[i])*len(wordList[i])

    if cnt != l :
        print("NO")
    else :
        print("YES")
