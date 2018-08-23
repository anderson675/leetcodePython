def isSelfDivisble(x):
    strNum = str(x)
    for ch in strNum:
        if ch =='0' or x%int(ch) != 0:
            return False

    return True

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left,right+1):
            if isSelfDivisble(num):
                ans.append(num)
        return ans


