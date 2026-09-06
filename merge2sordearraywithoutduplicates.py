nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,9,10]

def merge2sortedArray(nums1, nums2):
    i, j = 0, 0
    result = []
    n1, n2 = len(nums1), len(nums2)

    # Merge while both arrays have elements
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            if len(result) == 0 or nums1[i] != result[-1]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or nums2[j] != result[-1]:
                result.append(nums2[j])
            j += 1

    # Add remaining elements from nums1
    while i < n1:
        if len(result) == 0 or nums1[i] != result[-1]:
            result.append(nums1[i])
        i += 1

    # Add remaining elements from nums2
    while j < n2:
        if len(result) == 0 or nums2[j] != result[-1]:
            result.append(nums2[j])   # ✅ fixed: use nums2[j], not nums1[j]
        j += 1

    return result

print(merge2sortedArray(nums1, nums2))
