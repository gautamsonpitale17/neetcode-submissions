class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maximum = 0
        left = 0
        zeroes = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            maximum = max(maximum, right-left+1)

        return maximum