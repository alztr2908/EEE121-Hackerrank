def quick_sort(arr):
    # helper function
    quick_sort_ar(arr, 0, len(arr))

def quick_sort_ar(arr,start,end):
  # Base Case
  if end - start < 2:
    # single element base case
    return 
  
  # Set pivot at the start of the element
  pivot = i = start

  # Iterate at second item until last item
  for j in range(start+1,end):
    if arr[j] < arr[pivot]:
      i+=1
      arr[j],arr[i] = arr[i],arr[j]
  # Switch pivot and i
  arr[i], arr[pivot] = arr[pivot], arr[i]
  pivot = i
  # Left side of array
  quick_sort_ar(arr, start, pivot)
  # Right side of array
  quick_sort_ar(arr, pivot+1, end)

  return arr


# input handling
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

print(arr)
# quick sort function call
quick_sort(arr)
print(arr)

# output loop
# for i in arr:
#     print(i)
