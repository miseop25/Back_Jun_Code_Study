import copy
def solution(land):
    dp = land[0]
    for i in range(1, len(land)) :
        case = []
        n0,n1,n2,n3 = land[i][0], land[i][1], land[i][2], land[i][3]
        case.append(max(dp[1], dp[2],dp[3]) + n0)
        case.append(max(dp[0], dp[2], dp[3]) + n1)
        case.append(max(dp[0], dp[1], dp[3]) + n2)
        case.append(max(dp[0], dp[1], dp[2]) + n3)
        dp = copy.deepcopy(case)
    return max(dp)