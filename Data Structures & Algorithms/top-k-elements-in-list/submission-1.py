class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init map that counts how many times each number appears
        # init frequency list, where freq[i] will store all numbers that appear i times
        # iterate through nums, mapping each num : frequency of num
        # for each nums and its freq, add that number to freq list
        # init empty res list
        # loop from largest possible freq down to 1
            # for each num in freq[i], append to res list
            # once res contains k numbers, return it

        freqMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for key, val in freqMap.items():
            freq[val].append(key)
        res = []
        for x in range(len(freq) - 1, 0, -1):
            for num in freq[x]:
                res.append(num)
                if len(res) == k:
                    return res