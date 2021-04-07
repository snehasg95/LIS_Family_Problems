# [1,3,5,4,7]
# [1,3,5] - length 3 is the longest incraesing contigous subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
      
        # similar to contigous ones question
        
        # edge cases
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        max_len = 1
        seq_len = 1
        # each number itself is a LIS
        
        startIdx = 0
        
        for idx in range(1, len(nums)):
            
            if nums[idx] > nums[idx - 1]:
                seq_len += 1
                
                max_len = max(max_len, seq_len)
                
                
            else:
                seq_len = 1
   
        
        return max_len
        
        
        
        

        

