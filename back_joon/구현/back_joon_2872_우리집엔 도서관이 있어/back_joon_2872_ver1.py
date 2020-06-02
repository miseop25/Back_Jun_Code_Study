import sys
input = sys.stdin.readline

def soluction(num) :
    book_dict = dict()
    index_dict = dict()
    result = 0
    for i in range(num) :
        temp = int(input())
        book_dict[temp] = i
        index_dict[i] = temp
    
    for i in range(N-1, 0, -1) :
        index = book_dict[i]
        if index == N-1 :
            result += 1
            book_dict[i] = 0
            for j in range(index) :
                if index_dict[j] != i :
                    book_dict[index_dict[j]] += 1
            
            for k, v in book_dict.items() :
                index_dict[v] = k

        elif book_dict[index_dict[index + 1]] != i+1 :
            result += 1
            book_dict[i] = 0
            for j in range(index) :
                if index_dict[j] != i :
                    book_dict[index_dict[j]] += 1
            
            for k, v in book_dict.items() :
                index_dict[v] = k
    return result






if __name__ == "__main__":
    N = int(input())
    print(soluction(N))