class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def swap(self,i : int, j: int) -> None:
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def percolate_up(self, i : int) -> None:
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.swap(i,i//2)
            i = i//2
    
    def percolate_down(self, i : int)-> None:
        while 2 * i < len(self.heap):
            left,right = 2*i,2*i+1
            if (
                right < len(self.heap) and
                self.heap[right] < self.heap[left] and
                self.heap[right] < self.heap[i]
            ):
                self.swap(i,right)
                i = right
            elif ( self.heap[left] < self.heap[i] ):
                self.swap(i,left)
                i = left
            else:
                break

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.percolate_up(len(self.heap)-1)

    def pop(self) -> int:
        if len(self.heap) == 1: return -1
        if len(self.heap) == 2: return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)
        return res

    def top(self) -> int:
        if len(self.heap) == 1: return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if not nums: return
        nums.append(nums[0])
        self.heap = nums
        curr = (len(self.heap)-1)//2
        while curr > 0:
            self.percolate_down(curr)
            curr -= 1
        
        