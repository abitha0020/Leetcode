class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minval = nums[0]
        mindist = abs(nums[0])
        for i in nums:
            j=abs(i)
            if j<mindist:
                mindist=j
                minval=i
            if j==mindist:
                if minval<i:
                    minval=i    
        return minval        
        