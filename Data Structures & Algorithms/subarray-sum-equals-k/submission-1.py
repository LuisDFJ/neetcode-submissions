class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        complements = {0:1}
        total = 0
        count = 0
        for n in nums:
            total += n
            complement = total - k
            if complement in complements:
                count += complements[complement]
            if total not in complements:
                complements[total] = 0
            complements[total] += 1
        return count


            

        