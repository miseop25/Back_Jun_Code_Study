from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = nums.count(0)
        for _ in range(zero) :
            nums.remove(0)
            nums.append(0)
        print(nums)


a = Solution()
a.moveZeroes([1,2,0,7,6,0,0,3])
a.moveZeroes([1,2,3,4,5])
        