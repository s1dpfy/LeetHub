class Solution(object):
    def pivotIndex(self, nums):
        PrefixSum = [0 for _ in range(len(nums))]
        PrefixSum[0] = nums[0]
        for i in range(1,len(nums)):
            PrefixSum[i] = PrefixSum[i-1] + nums[i]
        pivot = 0
        for i in range(len(nums)):
            sum1 = 0 if i == 0 else PrefixSum[i-1]
            sum2 = 0 if i == len(nums)-1 else PrefixSum[len(nums)-1] - PrefixSum[i]
            if sum1 == sum2:
                 return i
        return -1
            
            