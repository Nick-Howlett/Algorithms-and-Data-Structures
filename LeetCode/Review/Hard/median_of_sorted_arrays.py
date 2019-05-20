class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = len(nums1), len(nums2)
        if x > y:
            nums1, nums2, x, y = nums2, nums1, y, x
        low = 0
        high = len(nums1)
        while low <= high:
            xmid = (low + high) // 2
            ymid = (x + y + 1) // 2 - xmid
            max_leftx = nums1[xmid - 1] if xmid else -math.inf
            min_rightx = nums1[xmid] if xmid != x else math.inf
            max_lefty = nums2[ymid - 1] if ymid else -math.inf
            min_righty = nums2[ymid] if ymid != y else math.inf
            
            if max_leftx <= min_righty and max_lefty <= min_rightx:
                return max(max_leftx, max_lefty) if (x + y) % 2 == 1 else (max(max_leftx, max_lefty) + min(min_rightx, min_righty)) / 2
            elif max_leftx > min_righty:
                high = xmid - 1
            else:
                low = xmid + 1
        return -1