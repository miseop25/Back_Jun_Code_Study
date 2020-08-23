if __name__ == "__main__":
    word = input().rstrip()
    result = list(word.split("-"))
    answer = ''
    for i in result :
        answer += i[0]
    print(answer)
