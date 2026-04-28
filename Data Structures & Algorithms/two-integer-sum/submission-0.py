class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = { }

        for i in range(n):
            needed = target - nums[i]

            if needed in hash_map:
                return[hash_map[needed], i]
            hash_map[nums[i]] = i
            
        