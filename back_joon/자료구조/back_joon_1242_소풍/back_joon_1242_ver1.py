def soluction() :
    answer = 0
    N, K, M = map(int, input().split(" "))
    if K == 1 :  return M

    while N > 0 :
        if M%K == 0 :
            answer += M//K
            return answer
        elif N < K :
            if K%N == 0 :
                if M == N :
                    return answer + 1
                else :
                    N -= 1
                    answer += 1
            elif K%N == M :
                return answer + 1
            else :
                if K%N < M :
                    M -= K%N
                else :
                    M = K%N - M + 1
                answer += 1
                N -= 1
        elif N == K :
            if M == N :
                return answer + 1
            else :
                N -= 1
        else :
            if (N//K)*K > M :
                M = M - (M//K)  + N%K
            else :
                M = M - (N//K)*K
            answer += N//K
            N -= N//K
    return answer + 1


if __name__ == "__main__":
    print(soluction())
    