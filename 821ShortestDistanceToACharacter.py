class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [0 if c == C else n for c in S] #set a res vector that only with two values: n or 0(find the C first)
        for i in range(n-1): res[i+1] = min(res[i+1], res[i]+1) #from left to right
        for i in range(n-1)[::-1]: res[i] = min(res[i], res[i+1]+1)
        return res
