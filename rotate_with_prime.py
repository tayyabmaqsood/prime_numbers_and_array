def swap(arr,j,k):
  temp = arr[j]
  arr[j] = arr[k]
  arr[k] = temp
  return arr

def is_prime(num):
  flag = False
  if num > 1:
      for i in range(2, num):
          if (num % i) == 0:
              flag = True
              break
  if flag:
      return False
  else:
      return True

def rotate_array(arr,i):
  if not (is_prime(arr[i])):
    j = i
    k = j-1
    while(k >= 0):
      while (is_prime(arr[k]) and k >= 0):
        k -= 1
      if k >= 0:
        arr = swap(arr,j,k)
        j = k
        k -= 1
  else:
    while(is_prime(arr[i]) and i >= 0 ):
      i -= 1
    rotate_array(arr,i)
  return arr
arr = [2,6,12,3,16,9,11,4,3,8,7,10]
print(rotate_array(arr,len(arr) - 1))

arr = [4,6,8,10,12,8]
print(rotate_array(arr,len(arr)-1))

