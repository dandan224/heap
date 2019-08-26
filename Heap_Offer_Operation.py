class Solution(object):

  def offerHeap(self, array, ele):
    """
    input: int[] array, int ele
    return: int[]
    """
    # write your solution here
    
    array.pop()
    array.append(ele)
    self.sift_up(array, len(array) -1)
    return array



  def sift_up(self, array, index):
      parent_index = (index - 1)//2
      if parent_index < 0 or array[index] > array[parent_index]:
        return
      array[index], array[parent_index] = array[parent_index], array[index]
      self.sift_up(array, parent_index)
