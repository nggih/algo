class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # tmp = s.split(" ")
        # print(tmp)
        # tmp = [i for i in tmp if len(i) > 0]
        # print(tmp)
        # return len(tmp[-1])
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

s = Solution()
string = "   fly me   to   the moon  "
res = s.lengthOfLastWord(string)
print(res)