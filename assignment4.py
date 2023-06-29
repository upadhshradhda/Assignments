# Question-1
def common_elements(arr1, arr2, arr3):
    result = []
    i = j = k = 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
result = common_elements(arr1, arr2, arr3)
print(result)  


# Question-2
def disinct_elements(nums1, nums2):
    distinct_nums1 = set(nums1) - set(nums2)
    distinct_nums2 = set(nums2) - set(nums1)
    return [list(distinct_nums1), list(distinct_nums2)]

nums1 = [1,2,3]
nums2 = [2,4,6]
answer = disinct_elements(nums1, nums2)
print(answer) 


# Question-3
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
matrix = [
    [1,2,3],[4,5,6],[7,8,9]
]

transposed_matrix = transpose(matrix)
for row in transposed_matrix:
    print(row)
    
    
# Question-4
def array_pair_sum(nums):
    nums.sort()  
    n = len(nums) // 2
    max_sum = 0

    for i in range(0, n * 2, 2):
        max_sum += nums[i]

    return max_sum
nums = [1,4,3,2]
maximized_sum = array_pair_sum(nums)
print(maximized_sum) 


# Question-5
def arrange_coins(n):
    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        curr = mid * (mid + 1) // 2

        if curr == n:
            return mid
        elif curr < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

n = 5
complete_rows = arrange_coins(n)
print(complete_rows)  


# Question-6
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    index = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    return result

nums = [-4,-1,0,3,10]
squared_nums = sorted_squares(nums)
print(squared_nums) 


# Question-7
def max_count(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col

M = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
ops = [[2, 2], [3, 3]]
max_integers = max_count(3, 3, ops)
print(max_integers)  


# Question-8
def array(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

nums = [2,5,1,3,4,7]
n = 3
shuffled_nums = array(nums, n)
print(shuffled_nums) 
