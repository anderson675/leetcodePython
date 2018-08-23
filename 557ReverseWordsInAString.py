class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2 = s.split(" ")
        answer = []
        for ch in s2:
            answer.append(ch[::-1])
        return ' '.join(answer) #character that joins the elements to make the lise a whole new string