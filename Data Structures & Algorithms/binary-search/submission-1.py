class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 0):
            return -1
        l = 0
        r = len(nums) - 1
        m = int((r-l)/2)
        print(f"m = {m}, -> {nums[m]}")
        if(nums[m] == target):
            # print(f"Found at {m}")
            return m
        elif(nums[m] > target):
            idx = self.search(nums[0:m], target)
            # print(f"Went left and got {idx}")
            return -1 if idx == -1 else idx
        else:
            idx = self.search(nums[m+1:r+1], target)
            # print(f"Went right and got {idx}")
            return -1 if idx == -1 else m+1+idx
        