class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right)//2

            if 0 < mid < n - 1:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif mid == 0:
                if n == 1 or nums[0] > nums[1]:
                    return 0
                else:
                    left = 1

            else: 
                if nums[n - 1] > nums[n - 2]:
                    return n - 1
                else:
                    right = n - 2