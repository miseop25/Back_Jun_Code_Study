import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    book = dict()
    for _ in range(N) :
        name = input().rstrip()
        if name in book :
            book[name] += 1
        else :
            book[name] = 1
    result = list(sorted(book.items(), key= lambda x: (-x[1], x[0]) ) )
    print(result[0][0])

