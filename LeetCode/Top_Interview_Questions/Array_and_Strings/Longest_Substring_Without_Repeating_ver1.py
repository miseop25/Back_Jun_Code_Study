class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '' :
            return 0
        alpabet = dict()
        answer = [-1, 0]
        for i in range(len(s)) :
            temp = s[i]
            if temp not in alpabet :
                alpabet[temp] = i
            else :
                comp = i - alpabet[temp]
                real = i - answer[1]
                # real = comp if comp > comp2 else comp2
                if real > answer[0] :
                    answer[0] = real
                alpabet[temp] = i
                answer[1] = i
        if answer[0] == -1 :
            return len(s)
        if answer[0] < len(s[answer[1]:]) :
            answer[0] = len(s[answer[1]:]) 
        return answer[0]
        