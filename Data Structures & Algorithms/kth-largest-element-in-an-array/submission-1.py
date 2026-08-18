class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        start,end = 0,len(nums)-1
        while start <= end:
            pointer = self.select( nums, start,end )
            if pointer == k: return nums[pointer]
            elif pointer < k:
                start = pointer + 1
            else:
                end = pointer - 1
        return -1
        

    def select(self, nums: List[int], start: int, end: int) -> int:
        def swap(i:int, j:int) -> None:
            nonlocal nums
            nums[i],nums[j] = nums[j],nums[i]
        pointer = start
        for i in range(start,end):
            if nums[i] < nums[end]:
                swap(i,pointer)
                pointer += 1
        swap(pointer,end)
        return pointer
