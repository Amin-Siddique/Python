## Time: O(n)
## Memory: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
## Take 1:

        #nums.sort()

        #for i in range(len(nums)-1):
        #    if nums[i] == nums[i+1]:
        #        return True               
        #    else:
        #        i+1
        
## Take 2:        
        #hashmap = {}
        
        #for idx,val in enumerate(nums):
        #    if nums[idx] in hashmap:
        #       return True
        #    else:
        #        idx + 1
        #        hashmap[val] = idx
 

## Take 3:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
                
