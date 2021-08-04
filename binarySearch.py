def recursive_binarySearch(arr,val):
  if len(arr) <= 1:
    print("asd")
    return arr[0] == val
  
  mid = len(arr)//2
  print(arr[:mid],mid)
  if arr[mid] == val:
    return True
  elif arr[mid] > val:
    return recursive_binarySearch(arr[0:mid], val)
  else:
    return recursive_binarySearch(arr[mid+1:], val)

def iterative_binarySearch(arr,val):
  start = 0
  end = len(arr)-1
  mid = len(arr)//2
  while  arr[mid] != val:
    if arr[mid] == val:
      return True
    elif arr[mid] < val:
      start = mid+1
      end = len(arr)-1
      mid = (end+start)//2
    else:
      start = 0
      end = mid-1
      mid =(end+start)//2
  return False

# print(recursive_binarySearch([1,2,3,4,5,6,7,8], 5))
# print(iterative_binarySearch([1,2,3,4,5,6,7,8], 3))


def binarySearch(arr,start,end,value):
  if start >= end:
    return False
  else:
    mid=(start+end)//2
    if arr[mid] == value:
      print(arr[mid],value)
      return True
    elif arr[mid] > value:
      return binarySearch(arr, start, mid-1, value)
    elif arr[mid] < value:
      return binarySearch(arr, mid+1, end, value)

arr= [1,2,3,4,5,6]
print(binarySearch(arr, 0, len(arr)-1, 10))

