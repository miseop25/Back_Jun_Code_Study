from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums :
            return nums
        nums.sort()
        answer = []
        cnt = 1
        comp = nums[0]
        for i in nums[1:] :
            if comp == i :
                cnt += 1
            else :
                if cnt == 2 :
                    answer.append(comp)
                cnt = 1
                comp = i
        if cnt == 2 :
            answer.append(comp)
        return answer


a = Solution()
print(a.findDuplicates([1,1,2]))
