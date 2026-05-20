class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # make a frequency arr for each string, 26 letters in english
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # append the freq arr for current str in the result map
            res[tuple(count)].append(s)
        return list(res.values())
        