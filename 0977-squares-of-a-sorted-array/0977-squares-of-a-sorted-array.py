class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Create left and right pointer:
        l, r = 0, len(nums)-1
        
        sqArr = []
        
        while len(sqArr) < len(nums):
        # Compare numbers at left and right:
            if nums[l]*nums[l] < nums[r]*nums[r]:
                sqArr.insert(0, nums[r]*nums[r])
                r -= 1
            else:
                sqArr.insert(0, nums[l]*nums[l])
                l += 1
                
        return sqArr