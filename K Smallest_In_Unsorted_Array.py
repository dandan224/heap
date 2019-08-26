#solution #1: order the array, then get the first k element
class Solution(object):
  def kSmallest(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # write your solution here
    import heapq
    if not array:
      return []
    # O(n)
    heapq.heapify(array)
    res = []
    # assume k would greater than the size of array
    #O(klogn)
    for i in range(min(k, len(array))):
      res.append(heapq.heappop(array))
    return res
  
 # time complexity: O(n + klogn)

#solution 2:
 # heapify the first k elements to form a max_heap of size = k   O(k)
  
 # iterate over the rest elements one by one, if the new element less the top, update  O((n - k)logk)
def kSmallest(array, k):
  if not array:
    return array
  if k >= len(array):
    return array
  res = [-elem for elem in array[0:k]]
  heapq.heapify(res)
  for i in range(k, len(array)):
    if array[i] < -res[0]:
      heapq.heappop(res)
      heapq.heappush(res, -array[i])
  return [-elem for elem in res]
