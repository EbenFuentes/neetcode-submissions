class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. init dict, key/values is nums[i] : frequency of #
        # 2. iterate through nums, add it to hashmap
        # 3. Sort by keys into a list, access the key's value, and reverse order so highest count is first
        # 3. return top k values from hashmap
        numToFreq = {}
        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        
        sorted_keys = sorted(
            numToFreq.keys(), key=lambda val: numToFreq[val], reverse=True
        )

        return sorted_keys[:k]
            

        