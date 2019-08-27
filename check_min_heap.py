class Solution(object):
  def isMinHeap(self, array):
    """
    input: int[] array
    return: boolean
    """
    # write your solution here
    if not array:
      return None
    """
    if len(array) == 1:
      return True
    if len(array) == 2:
      if array[0] > array[1]:
        return False
    """
    #if len(array) >= 3:
    for i in range(int((len(array)-2)/2)+1):
      if array[i] > array[i*2 +1] or (2*i +2 < len(array) and array[i] > array[i*2 + 2] ) :
        return False
    return True
