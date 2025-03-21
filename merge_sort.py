def merge_sort(list):
    # Sort a list in ascending order ,returns a new sorted list, divide: find the midpoint of the list and divide into sublists 
    # Conquer: Recursively sort the sublists created in previous step
    # Combine: Merge the sorted sublists created in previous step 
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists 
    Returns two sublists - left and right
  """
    
    mid = len(list)// 2
    left = list[:mid]
    right = list[mid:]

    return left,right 

def merge(left,right):
    # Merges two lists (arrays), sorting them in the process
    # Returns a new merged list

    l = []
    i= 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])