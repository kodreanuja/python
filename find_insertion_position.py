nums = [1, 3, 4, 5, 6]
target = int(input())
def searchInsert(nums, target):
        s = 0
        l = len(nums) - 1
        
        while s <= l:
            mid = (s + l) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                l = mid - 1
            else:
                s = mid + 1
            
        return s
print(searchInsert(nums, target))        
            
        