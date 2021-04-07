# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# Brute Force - Nested loops to find number sequences wont work as we may loose combinations
# Brute Force - Backtrack to get the combinations - notice we end up doing similar calculations 

# Optimise with DP
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        count = [1] * len(nums) # count at each number represents how many LIS we have
        arr = [1] * len(nums) # shows the number or length of LIS which in turn also breaks down to how many sub-seq are there -- note, they are all not longest
        
        result = 0
        # [1,3,5,4,7]
        for i in range(len(nums)): # new number as we consider sequences in the window
            
            for j in range(i): #comparing with previously seen numbers 
              
                if nums[i] > nums[j]:
                  # if the new addition is valid - valid only if it is > than prev number else it wont contribute to LIS
                    if arr[i] < arr[j] + 1:
                      # if the current length of seq at i is less than j + 1, it means we can include this number too in the sequence with prev number
                        arr[i] = arr[j] + 1
                        count[i] = count[j]
                        
                    elif arr[i] == arr[j] + 1:
                      # if it is same, then cumulatively add the previous count( i.e how many such length sequences we have
                        count[i] += count[j]
        
        
#         print(arr)
#         print(count)

        max_seen = arr[0]
        result = count[0]
        for idx in range(1, len(arr)):
            if arr[idx] > max_seen:
                max_seen = arr[idx]
                result = count[idx]
                
            elif arr[idx] == max_seen:
                result += count[idx]
                
        return result
            
            
                    
# nums = [1, 3, 4, 5, 7]
# arr =  [1, 2, 3, 4, 5] 
# here at number 7, the number 5 represents the length of the LIS possible ie 1,3,4,5,7
# at number 5, the number 4 represents length of LIS possible, ie 1,3,4,5 - length = 4


        
