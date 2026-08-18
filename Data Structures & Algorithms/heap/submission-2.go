type MinHeap struct {
    Heap []int
}

func NewMinHeap() *MinHeap {
    return &MinHeap {Heap:[]int{0}}
}

func (mh *MinHeap) swap(i,j int) {
    mh.Heap[i],mh.Heap[j] = mh.Heap[j], mh.Heap[i]
}

func (mh *MinHeap) percolate_up(i int) {
    for i > 1 && mh.Heap[i] < mh.Heap[i/2] {
        mh.swap(i,i/2)
        i = i/2
    }
}

func (mh *MinHeap) percolate_down(i int) {
    for 2*i < len(mh.Heap) {
        left, right := 2*i,2*i+1
        child := left
        if right < len(mh.Heap) && mh.Heap[right] < mh.Heap[left] {
            child = right
        }

        if mh.Heap[child] < mh.Heap[i] {
            mh.swap(i,child)
            i = child
        } else {
            break
        }
    }
}

func (mh *MinHeap) Push(val int) {
    mh.Heap = append(mh.Heap,val)
    mh.percolate_up(len(mh.Heap) - 1)
}

func (mh *MinHeap) Pop() int {
    if len(mh.Heap) == 1 { return -1 }

    res := mh.Heap[1]
    mh.Heap[1] = mh.Heap[len(mh.Heap)-1]
    mh.Heap = mh.Heap[:len(mh.Heap)-1]
    if len(mh.Heap) > 1 {
        mh.percolate_down(1)
    }
    return res
}

func (mh *MinHeap) Top() int {
    if len(mh.Heap) == 1 { return -1 }
    return mh.Heap[1]
}

func (mh *MinHeap) Heapify(nums []int) {
    mh.Heap = append([]int{0}, nums...)
    for i := len(mh.Heap)/2 ; i > 0 ; i-- {
        mh.percolate_down(i)
    }
}
