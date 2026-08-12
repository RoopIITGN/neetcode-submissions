class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = nums[0]

        while(True):
            s = nums[s]
            f = nums[nums[f]]
            if(s == f):
                break
        
        s2 = nums[0]
        while(s2 != s):
            s = nums[s]
            s2 = nums[s2]
        
        return s