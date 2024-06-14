class Solution(object):
    
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        minIncrement = 0
        maxnum = 0
        for num in nums:
            maxnum = max(maxnum,num)
            minIncrement += maxnum - num 
            maxnum += 1
        return minIncrement
