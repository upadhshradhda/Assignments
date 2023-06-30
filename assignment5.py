# Question-1
def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []  
    result = [[0] * n for _ in range(m)]

    for i in range(len(original)):
        row = i // n 
        col = i % n  
        result[row][col] = original[i]  
    return result
original = [1, 2, 3, 4] 
m = 2  
n = 2
result = convert_to_2d_array(original, m, n)
print(result)


# Question-2
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


# Question-3
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


# Question-4
def disinct_elements(nums1, nums2):
    distinct_nums1 = set(nums1) - set(nums2)
    distinct_nums2 = set(nums2) - set(nums1)
    return [list(distinct_nums1), list(distinct_nums2)]

nums1 = [1,2,3]
nums2 = [2,4,6]
answer = disinct_elements(nums1, nums2)
print(answer) 


# Question-5
def distance_value(arr1, arr2, d):
    distance = 0
    for num1 in arr1:
        found = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break
        if not found:
            distance += 1
    return distance
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
result = distance_value(arr1, arr2, d)
print(result)


# Question-6
def find_duplicates(nums):
    duplicates = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            duplicates.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return duplicates
nums = [4, 3, 2, 7, 8, 2, 3, 1] 
result = find_duplicates(nums)
print(result)


# Question-7
def find_minimum(nums):
    left = 0
    right = len(nums) - 1
    if nums[left] <= nums[right]:
        return nums[left]
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

nums = [3,4,5,1,2] 
result = find_minimum(nums)
print(result)


# Question-8
def find_original_array(changed):
    original = sorted(changed) 
    for num in changed:
        if num % 2 != 0:
            return []
        half_num = num // 2
        if half_num in original:
            original.remove(half_num)
        else:
            return []
    return original
changed = [1,3,4,2,6,8] 
result = find_original_array(changed)
print(result)


