class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        mid = length//2
        arr = []
        count = 0
        
        while count <= mid:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    arr.append(nums1.pop(0))
                else:
                    arr.append(nums2.pop(0))
            elif nums1:
                remain = mid - len(arr) + 1
                arr.extend(nums1[:remain])
                break
            else:
                remain = mid - len(arr) + 1
                arr.extend(nums2[:remain])
                break
            count += 1
        
        if length %2 == 0:
            return (arr[mid-1] + arr[mid])/2
        else:
            return arr[mid]


# Time Complexity: O()
# Space Complexity: O((m*n)/2)