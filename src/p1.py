### Problem 1 - Sorting

# Given a list of random unordered numbers, write a function that sort them in ascending order.

# Input: 21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28

# Expected output: -36, -16, -3, 8, 21, 28, 55, 77, 99, 111, 400

# Note:
# - You are not allowed to use language library function to solve the problem.
# - **Bonus**: Prepare space-time complexity analysis for your solution.

def merge_sort(list):
  if len(list) <= 1:
    return list

  mid = len(list) // 2
  left = merge_sort(list[:mid])
  right = merge_sort(list[mid:])
  return merge(left, right)

def merge(left, right):
    result = []
    left_ind = right_ind = 0

    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] <= right[right_ind]:
            result.append(left[left_ind])
            left_ind += 1
        else:
            result.append(right[right_ind])
            right_ind += 1

    result.extend(left[left_ind:])
    result.extend(right[right_ind:])
    return result

input = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]

print(merge_sort(input))