class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        stack = [] # tuple (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                max_rect = max(max_rect, (i-ind)*height)
                start = ind
            stack.append((start, h))

        for i, h in stack:
            max_rect = max(max_rect, (len(heights)-i)*h)
        return max_rect