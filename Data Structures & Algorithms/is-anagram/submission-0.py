class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = [0]*26
        countT = [0]*26
        for i in range(len(s)):
            indexS = ord(s[i]) - ord('a')
            indexT = ord(t[i]) - ord('a')

            countS[indexS] += 1
            countT[indexT] += 1

        return countS == countT