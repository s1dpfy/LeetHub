class Solution(object):
    def longestOnes(self, nums, k):
        left = 0 
        right = k
        maxlength = k
        real = maxlength
        zerocount = nums[left:right].count(0)
        while right < len(nums):
            if nums[right] == 0:
                zerocount += 1
                if zerocount > k:
                    while True:
                        maxlength -= 1
                        if nums[left] == 0:
                            left += 1
                            zerocount -= 1
                            break
                        left += 1
            right += 1
            maxlength += 1
            real = max(real,maxlength)
        return real