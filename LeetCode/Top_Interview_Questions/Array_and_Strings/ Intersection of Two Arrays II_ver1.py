from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = nums1 if len(nums1) > len(nums2) else nums2
        y = nums1 if len(nums1) <= len(nums2) else nums2
        answer = []
        x.sort()
        y.sort()

        while y and x:
            temp = y.pop()
            while x[-1] > temp :
                x.pop()
                if not x : break
            if not x : break
            if x[-1] == temp :
                answer.append(x.pop())
        return answer
    

t = Solution()
print(t.intersect([4,3,9,3,1,9,7,6,9,7],[5,0,8]))