from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        anchor = strs[0]

        res = ""
        
        for i in range(len(anchor)):
            for s in strs:
                if i == len(s) or s[i] != anchor[i]:
                    return res
            res += anchor[i]

        return res 