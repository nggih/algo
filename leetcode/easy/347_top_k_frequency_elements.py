from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and k == 1:
            return nums
        container = {}
        for i in nums:
            if i not in container:
                container[i] = 1
            else:
                container[i] += 1
        print(container)
        result = sorted(container.items(), key=lambda x:x[1], reverse=True)
        final = [i[0] for i in result] 
        return final[:k]
        

s = Solution()

nums = [1,1,1,2,2,3]
k = 2
result = s.topKFrequent(nums, k)
print(result)