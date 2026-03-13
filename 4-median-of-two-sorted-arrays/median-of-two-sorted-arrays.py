class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two arrays
        arr = nums1 + nums2
        # Sort the merged array
        arr.sort()
        n = len(arr)
        # If odd length → middle element
        if n % 2 == 1:
            return arr[n // 2]
        # If even length → average of two middle elements
        else:
            return (arr[n // 2] + arr[n // 2 - 1]) / 2