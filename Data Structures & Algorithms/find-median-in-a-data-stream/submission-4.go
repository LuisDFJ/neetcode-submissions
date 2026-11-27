type MinHeap []int

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i,j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i,j int) { h[i],h[j] = h[j],h[i] }
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	l := len(old)
	x := old[l-1]
	*h = old[:l-1]
	return x
}

type MaxHeap []int

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i,j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i,j int) { h[i],h[j] = h[j],h[i] }
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	l := len(old)
	x := old[l-1]
	*h = old[:l-1]
	return x
}

type MedianFinder struct {
	top *MinHeap
	bottom *MaxHeap
}



func Constructor() MedianFinder {
	top := &MinHeap{}
	bottom := &MaxHeap{}
	heap.Init(top)
	heap.Init(bottom)
	return MedianFinder {
		top: top,
		bottom: bottom,
	}
}


func (this *MedianFinder) AddNum(num int)  {
	if this.top.Len() > 0 {
		if num > (*this.top)[0] {
			heap.Push(this.top, num)
		} else {
			heap.Push(this.bottom, num)
		}
	} else {
		heap.Push(this.top, num)
	}
	// Rebalancing Step
	if this.top.Len() > this.bottom.Len() + 1 {
		heap.Push(this.bottom, heap.Pop(this.top))
	}
	if this.bottom.Len() > this.top.Len() + 1 {
		heap.Push(this.top, heap.Pop(this.bottom))
	}
}


func (this *MedianFinder) FindMedian() float64 {
	if this.top.Len() > this.bottom.Len() {
		return float64((*this.top)[0])
	} else if this.top.Len() < this.bottom.Len() {
		return float64((*this.bottom)[0])
	} else {
		return float64((*this.top)[0] + (*this.bottom)[0])/2
	}
}
