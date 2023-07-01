class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        l1 = len(str1)
        l2 = len(str2)

        for i in range(l2, 0, -1):
            print('i:', i)
            print("l1, l2: ", l1, l2)
            print("l1%i", l1 % i)
            print("l2%i", l2 % i)
            if l1 % i == 0 and l2 % i == 0:
                c = str2[:i]
                print("c:", c)
                print("l1/i", int(l1/i))
                print("l2/i", int(l2/i))
                print(c * int(l1/i))
                print(c * int(l2/i))
                if c * int(l1/i) == str1 and c * int(l2/i) == str2:
                    return c
            print("____")

        return ""

str1 = "ABABAB"
str2 = "ABAB"

s = Solution()

result = s.gcdOfStrings(str1, str2)
print('result',result)