nums1 = [1,3, 45,76,78]
nums2 = [2, 4]

def findMedianSortedArrays(nums1, nums2) :
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = half_len - partition_nums1
            
            nums1_max_left = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            nums1_min_right = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            
            nums2_max_left = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            nums2_min_right = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            
            if nums1_max_left <= nums2_min_right and nums2_max_left <= nums1_min_right:
                if (m + n) % 2 == 0:
                    return (max(nums1_max_left, nums2_max_left) + min(nums1_min_right, nums2_min_right)) / 2.0
                else:
                    return max(nums1_max_left, nums2_max_left)
            elif nums1_max_left > nums2_min_right:
                right = partition_nums1 - 1
            else:
                left = partition_nums1 + 1

print(findMedianSortedArrays(nums1, nums2))