class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        a = []
        a.append(nums[0])
        for i in range(1,len(nums)):
            if a[i-1] < 0:
                    a.append(nums[i])
            else:
                    a.append(a[i-1]+nums[i])
        return max(a)