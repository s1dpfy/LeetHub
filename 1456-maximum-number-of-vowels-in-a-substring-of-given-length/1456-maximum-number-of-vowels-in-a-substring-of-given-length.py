class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_sum, sum = 0, 0
        i, j = 0, 0
        
        while j < len(s):
            if s[j] in vowels:
                sum += 1
                
            if j-i+1 == k:
                max_sum = max(max_sum, sum)
                if s[i] in vowels:
                    sum -= 1
                i += 1

            j += 1
        
        return max_sum