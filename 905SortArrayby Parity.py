class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for num in A:
            if num%2 != 0:
                odd.append(num)
            else:
                even.append(num)
        even.append(odd)
        return even


