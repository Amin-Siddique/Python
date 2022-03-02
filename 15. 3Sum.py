# Time : O(n2)
# Memory : O(n) #Depends on Sorting 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        ##     l        r
        ##[-4,-1,-1,0,1,2]
        
        for i,val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i + 1, len(nums) -1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0 :
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1      # scenario: [-2,-2,0,2,2]
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
                    
                
