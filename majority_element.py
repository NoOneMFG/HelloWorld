class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)/2
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>l:
                return i
