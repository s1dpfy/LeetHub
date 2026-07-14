class Solution(object):
    def longestSubarray(self, nums):
        left,right = 0,1
        havezero = 1 if nums[left:right].count(0) else 0
        maxlenght = 1
        while right < len(nums):
            if nums[right] == 0:
                havezero += 1
                if havezero == 2:
                    while True:
                        if nums[left] == 0:
                            left += 1
                            havezero = 1
                            break
                        left += 1
            right += 1
            maxlenght = max(maxlenght,right-left)
        return maxlenght - 1