class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        post1 = -1
        post2 = -1 
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                post1 = mid         
                right = mid - 1    
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                post2 = mid         
                left = mid + 1    
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [post1, post2]


nums = [5,7,7,8,8,10]
target = 8

obj = Solution()
print(obj.searchRange(nums, target))