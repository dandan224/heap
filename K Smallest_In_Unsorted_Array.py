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
    heapq.heapify(array)
    res = []
    # assume k would greater than the size of array
    for i in range(min(k, len(array))):
      res.append(heapq.heappop(array))
    return res
