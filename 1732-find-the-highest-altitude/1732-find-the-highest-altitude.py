class Solution(object):
    def largestAltitude(self, gain):
        from collections import deque
        gain = deque(gain)
        gain.appendleft(0)
        n = len(gain)
        prefixSum = [0]*n 
        prefixSum[0] = gain[0] 
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + gain[i]
        return max(prefixSum)