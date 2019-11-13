def solution(numbers):
    numbers = [*map(str,numbers)]
    numbers.sort(key = lambda x : x*3, reverse = True)
    g= lambda x : x*3
    print(g('3'))
    return str(int(''.join(numbers)))


ta = [3, 30, 34, 5, 9]
a =solution(ta)
print(a)