import sys
input = sys.stdin.readline

def soluction(num) :
    books = []
    result = 0
    for i in range(num) :
        books.append( int(input()))
    
    cnt  = 1
    check = False
    for i in range(len(books)-1, -1, -1 ) :
        tenp = books[i]
        if tenp == N :
            check = True
        if check :
            if books[i] == num -1 :
                cnt += 1
                num -= 1
    result = len(books) - cnt
    return result


if __name__ == "__main__":
    N = int(input())
    print(soluction(N))