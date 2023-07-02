from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1 
        # reverse iteration
        # new max = max(old_max, arr[i])

        right_max = -1
        for i in range(len(arr) -1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        
        return arr


        # res = []
        # length = len(arr)
        # if length == 1:
        #     return [-1]
        # for i in range(1, length):
        #     tmp = max(arr[i:])
        #     res.append(tmp)
        #     if i == length-1:
        #         res.append(-1)
        # return res 


s = Solution()
arr = [17,18,5,4,6,1]
result = s.replaceElements(arr)
print('result:',result)

arr = [400]
result = s.replaceElements(arr)
print('result:',result)