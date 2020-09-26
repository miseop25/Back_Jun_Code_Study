import sys
input = sys.stdin.readline


if __name__ == "__main__":
    word = input().rstrip()

    st = 0
    index = 10
    length = len(word)

    while index < length :
        print(word[st:index])
        st = index
        index += 10
    print(word[st:])