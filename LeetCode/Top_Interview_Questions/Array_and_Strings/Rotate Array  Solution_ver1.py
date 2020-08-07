from typing import List
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums = deque(nums)
        for _ in range(k) :
            temp = nums.pop()
            nums.appendleft(temp)
