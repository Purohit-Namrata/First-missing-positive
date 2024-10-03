from typing import List
class Solution:
    def fistMissingPositive(self, nums: List[int]) -> int:
        ans=1
        seen=set()
               
        for i in nums:    
            seen.add(i)
            while ans in seen:
                ans+=1
        return ans

s=Solution()
print("First missing positive number is: ",s.fistMissingPositive([1,-2,3,4,5]))
    

