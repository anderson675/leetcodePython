class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in range(len(A)):
            A[row] = A[row][::-1]
            for col in range(len(A[0])):
                A[row][col] ^= 1
        return A
