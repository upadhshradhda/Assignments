# Question-1
def permutation(s):
    n = len(s)
    perm = []
    low, high = 0, n

    for i in range(n):
        if s[i] == 'I':
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1
    perm.append(low)

    return perm
s = "IDID"
result = permutation(s)
print(result)


# Question-2
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // cols][mid % cols]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target = 3
result = searchMatrix(matrix, target)
print(result)


# Question-3
def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False
    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1
    return i == n - 1
arr = [2,1] 
print(validMountainArray(arr))  


# Question-4
def findMaxLength(nums):
    count = 0
    max_length = 0
    count_map = {0: -1} 
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count in count_map:
            length = i - count_map[count]
            max_length = max(max_length, length)
        else:
            count_map[count] = i
    return max_length
nums = [0,1]
print(findMaxLength(nums))  


# Question-5
def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    min_sum = 0
    for i in range(len(nums1)):
        min_sum += nums1[i] * nums2[i]
    return min_sum
nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
print(minProductSum(nums1, nums2))


# Question-6
from collections import defaultdict
def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  
    freq_map = defaultdict(int)
    original = []
    for num in changed:
        freq_map[num] += 1
    for num in sorted(changed):
        if freq_map[num] == 0:
            continue
        if freq_map[2 * num] == 0:
            return []  
        original.append(num)
        freq_map[num] -= 1
        freq_map[2 * num] -= 1
    return original
changed = [1,3,4,2,6,8]
print(findOriginalArray(changed)) 


# Question-7
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom = 0, n - 1  
    left, right = 0, n - 1  
    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix
n = 3
result = generateMatrix(n)
for row in result:
    print(row)


# Question-8
def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                for l in range(n):
                    if mat2[j][l] != 0:
                        result[i][l] += mat1[i][j] * mat2[j][l]
    return result
mat1 = [
    [1, 0, 0],
    [-1, 0, 3]
]
mat2 = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
result = multiply(mat1, mat2)
for row in result:
    print(row)
