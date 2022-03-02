#Time Complexity: O(n)
#Memory Complexity: O(n) #Due to HashMap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using Hash Map to do one pass. 
        prevMap = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i ] 
            prevMap[n] = i
        return
      
      
      
      #https://leetcode.com/problems/two-sum/
