class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i >= max(nums2[nums2.index(i):]):
                res.append(-1)
            else:
                for j in nums2[nums2.index(i):]:
                    if i < j:
                        res.append(j)
                        break
        return res