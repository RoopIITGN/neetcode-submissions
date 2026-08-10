class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l <= r):
            m = (l+r)//2
            if(target < nums[m]):
                if(target >= nums[l]) or (nums[m] < nums[l]):
                    r = m-1
                elif(target <= nums[r]):
                    l = m+1
                else:
                    return -1
            elif(target > nums[m]):
                if(target <= nums[r]) or (nums[m] > nums[r]):
                    l = m+1
                elif(target >= nums[l]):
                    r = m-1
                else:
                    return -1
            else:
                return m
        return -1