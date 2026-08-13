type DynamicArray struct {
    arr []int
    capacity int
    size int
}

func NewDynamicArray(capacity int) *DynamicArray {
    da := DynamicArray{}
    da.arr = make([]int,capacity)
    da.capacity = capacity
    da.size = 0
    return &da
}

func (da *DynamicArray) Get(i int) int {
    return da.arr[i]
}

func (da *DynamicArray) Set(i int, n int) {
    da.arr[i] = n
}

func (da *DynamicArray) Pushback(n int) {
    if da.size == da.capacity {
        da.resize()
    }
    da.arr[da.size] = n
    da.size += 1
}

func (da *DynamicArray) Popback() int {
    da.size -= 1
    return da.arr[da.size]
}

func (da *DynamicArray) resize() {
    da.capacity *= 2
    arr := make([]int,da.capacity)
    for i,n := range da.arr {
        arr[i] = n
    }
    da.arr = arr
}

func (da *DynamicArray) GetSize() int {
    return da.size
}

func (da *DynamicArray) GetCapacity() int {
    return da.capacity
}
