def is_palindrome(num):
    return str(num)[:: -1] == str(num)

def solution(num):
  arr = []
  for i in range(100, num):
      for j in range(100, num):
          if is_palindrome(i * j):
              arr.append(i * j)
  return max(arr)

print(solution(1000))