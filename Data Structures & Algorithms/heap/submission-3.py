class MinHeap:
    def __init__(self):
        self.heap = [0]
    
    def _swap(self,i:int,j:int):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def _percolate_up(self, i:int):
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self._swap(i,i//2)
            i = i // 2
    def _percolate_down(self, i:int):
        while 2 * i < len(self.heap):
            left,right = 2*i, 2*i + 1
            if (
                right < len(self.heap) and
                self.heap[right] < self.heap[left] and
                self.heap[right] < self.heap[i]
            ):
                self._swap(i,right)
                i = right
            elif self.heap[left] < self.heap[i]:
                self._swap(i,left)
                i = left
            else:
                break

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._percolate_up(len(self.heap)-1)

    def pop(self) -> int:
        if len(self.heap) == 1: return -1
        if len(self.heap) == 2: return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._percolate_down(1)
        return res

    def top(self) -> int:
        if len(self.heap) > 1: return self.heap[1]
        return -1

    def heapify(self, nums: List[int]) -> None:
        if not nums: return
        nums.append(nums[0])
        self.heap = nums
        i = (len(self.heap)-1)//2
        while i > 0:
            self._percolate_down(i)
            i -= 1