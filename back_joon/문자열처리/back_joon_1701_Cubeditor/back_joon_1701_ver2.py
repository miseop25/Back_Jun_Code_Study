def makeTable(word) :
    table = [0 for _ in range(len(word)) ]
    j = 0
    for i in range(1, len(word)) :
        while j > 0 and word[i] != word[j] :
            j = table[j-1]
        if word[i] == word[j] :
            j += 1
            table[i] = j
    return table
        

if __name__ == "__main__":
    s = input().rstrip()
    answer = []
    for i in range(len(s)) :
        answer.append(max(makeTable(s[i :])))
    print(max(answer))
