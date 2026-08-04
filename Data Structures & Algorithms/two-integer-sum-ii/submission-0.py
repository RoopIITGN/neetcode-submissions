class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le, ri = 0, len(numbers) - 1
        while(le < ri):
            if((numbers[le] + numbers[ri]) == target):
                return [le + 1, ri + 1]
            if((numbers[le] + numbers[ri]) > target):
                ri -= 1
            else:
                le += 1
        return []