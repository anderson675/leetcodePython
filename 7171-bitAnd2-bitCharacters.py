class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        size = len(bits)
        index = 0
        while index < size:
            if bits[index] == 1:
                flag = False
                index += 2
            else:
                flag = True
                index +=1
        return flag