class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = dict()
        for e in nums:
            if e in d:
                d[e] += 1
            else:
                d[e] = 1
        
        values = list(d.values())
        max_freq = max(values)
        in_total = values.count(max_freq)
        return in_total * max_freq