class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check: if s and t are not of same length, they are not an anagram
        if (len(s) != len(t)):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
        