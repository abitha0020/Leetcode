class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        res=[]
        while i<len(nums):
            start=nums[i]
            while i<len(nums)-1 and nums[i]+1==nums[i+1]:
                i=i+1
            if start==nums[i]:
                res.append(str(nums[i]))
            else:
                res.append(str(start)+"->"+str(nums[i]))  
            i=i+1  
        return res  