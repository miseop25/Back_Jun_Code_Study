def soluction(n) :

    if n <= 99 :
        return n
    elif n == 100 :
        return 99
    elif n == 1000 :
        return 144
    answer = 99
    han_dict = {
        1: [111,123,135,147,159], 2: [210,222,234,246,258], 3: [321,333,345,357,369],
        4: [420,432,444,456,468], 5: [531,543,555,567,579], 6: [630,642,654,666,678],
        7: [741,7536,765,777,789], 8: [840,852,864,876,888], 9: [951,963,975,987,999]
    }
    k = n//100
    answer += 5*(k-1)
    for i in han_dict[k] :
        if i <= n :
            answer += 1
    return answer


N = int(input())
print(soluction(N))
