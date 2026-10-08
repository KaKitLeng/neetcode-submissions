class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # index of the temp

        for i, t in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind = stack.pop()
                res[ind] = i-ind
            stack.append(i)
        return res






        