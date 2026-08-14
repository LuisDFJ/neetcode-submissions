func distance(point[]int) int {
    return point[0]*point[0] + point[1]*point[1]

}

func partition(points [][]int, s,e int) int {
    left := s
    pivot := distance(points[e])
    for i := s; i < e; i++ {
        if distance(points[i]) < pivot {
            points[i], points[left] = points[left], points[i]
            left += 1
        }
    }
    points[e], points[left] = points[left], points[e]
    return left
}

func kClosest(points [][]int, k int) [][]int {
    s,e := 0, len(points) - 1
    for s <= e {
        pivot := partition(points,s,e)
        if pivot == k {
            break
        } else if pivot < k {
            s = pivot + 1
        } else {
            e = pivot - 1
        }
    }
    return points[:k]
}
