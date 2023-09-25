class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        check if it is a e i o u
        h -> check a e i o u
        append with index
        """
        idxs = []


        for idx, i in enumerate(s.lower()):
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                idxs.append(idx)

        sorted_idxs = idxs.sorted()
        print(sorted_idxs)
        print(idxs)


s = "hello"

solution = Solution()
solution.reverseVowels(s)

s = "leetcode"
solution = Solution()
solution.reverseVowels(s)