class Solution:
    def __init__(self) :
        self.dp = [1,3,6]

    def updateDP(self, num: int) -> None :
        index = len(self.dp) + 1
        while self.dp[-1] <= num :
            self.dp.append(self.dp[-1]+ index)
            index += 1


    def arrangeCoins(self, n: int) -> int:
        if self.dp[-1] <= n :
            self.updateDP(n)
            return len(self.dp) - 1
        for i , val in enumerate(self.dp):
            if val > n :
                return i



t = Solution()
print(t.arrangeCoins(5))
print(t.arrangeCoins(1))