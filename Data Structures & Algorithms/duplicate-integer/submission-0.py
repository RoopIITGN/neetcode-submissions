class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in range(len(nums)):
            if nums[i] not in store:
                store.add(nums[i])
            else:
                return True
        return False