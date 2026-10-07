class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init l/r pointer
        l, r = 0, len(nums) - 1

        while l <= r:
            # compute mid
            mid = (l + r) // 2
            ## possible mid value is target, check it
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    # search in right portion
                    l = mid + 1
                else:
                    # search in left portion
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    # search in left potion
                    r = mid - 1
                else:
                    # search in right portion
                    l = mid + 1
        return -1
            
        