class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                # print(f"Entered while when i = {i}")
                prev_h = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                # print(f"cur_area = {prev_h*width}")
                max_area = max(max_area, prev_h * width)
                # print(f"max_area = {max_area}")
            stack.append(i)

        return max_area