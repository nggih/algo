nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1_tmp = nums1[:m]
nums2_tmp = nums2[:n]
all_tmp = nums1_tmp + nums2_tmp
nums1 = sorted(nums1[:m] + nums2[:n])
print(nums1)