def merge_sort(list):
    # Sort a list in ascending order ,returns a new sorted list, divide: find the midpoint of the list and divide into sublists 
    # Conquer: Recursively sort the sublists created in previous step
    # Combine: Merge the sorted sublists created in previous step
    #  Takes 0( log n ) time
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
            i += 1
        else:
          l.append(right[j])
          j += 1  


    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j+= 1        

    return l 

alist =  [54, 62, 93, 18, 76, 32, 45, 56, 21]
l = merge_sort(alist)

# print(l)

def verify_sort(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sort(list[1:])

print(verify_sort(alist))
print(verify_sort(l))
# Takes overall 0(log n) time
# Runs in overall 0(n) time