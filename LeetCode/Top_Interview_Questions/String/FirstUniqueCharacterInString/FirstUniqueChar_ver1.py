class Solution:
    def firstUniqChar(self, s: str) -> int:
        bfs = [0]*26
        if len(s) == 0 :
            return -1
        for i in s :
            bfs[ord(i)-97] += 1
        for i in range(len(s)) :
            if bfs[ord(s[i])-97] == 1 :
                return i
        return -1
        

a = Solution()
print(a.firstUniqChar("loveleetcode"))