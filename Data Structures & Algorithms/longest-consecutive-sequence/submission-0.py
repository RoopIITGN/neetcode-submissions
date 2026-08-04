class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_l = 0
        for n in num_set:
            if (n-1) not in num_set:
                cur = n
                cur_l = 1
                while(cur + 1 in num_set):
                    cur += + 1
                    cur_l += 1
                max_l = max(max_l, cur_l)
        return max_l