from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        sorted_nums = sorted(nums)
        print(sorted_nums)
        count = 1 
        anchor = 0
        for i in range(0, len(sorted_nums)-1):
            if sorted_nums[i-1] == sorted_nums[i] - 1: 
                count += 1
                # print(anchor)
            if sorted_nums[i-1] != sorted_nums[i] - 1:
                print('start of seq:',sorted_nums[i])

        return count 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        print(num_set)
        longest = 0

        for n in nums:
            if (n-1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)

        return longest


s = Solution()

nums = [100,4,200,1,3,2]
res = s.longestConsecutive(nums)
print(res)
nums =  [0,3,7,2,5,8,4,6,0,1, 10, 13, 14,15,16] 
res = s.longestConsecutive(nums)
print(res)
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
res = s.longestConsecutive(nums)
print(res)