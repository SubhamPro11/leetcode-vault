class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        min_num = min(nums)
        max_num = max(nums)
        
        freq = [0] * (max_num - min_num + 1)
        
        for n in nums:
            freq[n - min_num] += 1
        i = 0
        for val, count in enumerate(freq):
            while count > 0:
                nums[i] = val + min_num
                i += 1
                count -= 1
                
        return nums
