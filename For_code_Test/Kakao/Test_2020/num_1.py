def solution(board, moves):
    answer = 0
    basket = []
    N = len(board)

    for i in moves :
        for j in range(N) :
            buf = board[j][i-1]
            if buf != 0 :
                L = len(basket)
                if L != 0 :
                    comp = basket[L-1]
                    if buf == comp:
                        basket.pop()
                        answer = answer +2
                        board[j][i-1] = 0
                        break
                    else :
                        basket.append(buf)
                        board[j][i-1] = 0
                        break

                else :
                    basket.append(buf)
                    board[j][i-1] = 0
                    break
                    
            
    return answer


bs = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
m = [1,5,3,5,1,2,1,4]
print(solution(bs,m))