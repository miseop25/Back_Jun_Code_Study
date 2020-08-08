from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        change = list(map(str, digits))
        num = int("".join(change))
        num += 1 
        answer = list(str(num))
        return answer