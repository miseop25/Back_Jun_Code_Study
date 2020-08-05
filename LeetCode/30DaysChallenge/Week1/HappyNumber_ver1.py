class Solution:
    def isHappy(self, n: int) -> bool:
        numSets = set()
        while True :
            nums = list(map(int, list(str(n))))
            n = 0
            for i in nums :
                n += i*i
            if n == 1 :
                return True
            
            if n in numSets : 
                return False
            numSets.add(n)

            
            
            