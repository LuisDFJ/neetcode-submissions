from heapq import heappush, heappop

def distance(a : List[int]) -> float:
    return a[0]** 2 + a[1]** 2 # Square Root is not necessary
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s,e = 0,len(points) - 1
        left = -1
        while s <= e:
            left = self.partition(points,s,e)
            if left == k: break
            elif left < k:
                s = left + 1
            else:
                e = left - 1
        return points[:k]
    
    def partition(self,arr: List[List[int]], s: int, e:int) -> int:
        left = s
        for i in range(s,e):
            if distance(arr[i]) <= distance(arr[e]):
                arr[i],arr[left] = arr[left],arr[i]
                left += 1
        arr[e],arr[left] = arr[left],arr[e]
        return left