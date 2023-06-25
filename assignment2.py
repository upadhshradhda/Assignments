#Question-1
def PairSum(nums):
    nums.sort()  
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]  
    return max_sum

nums = [1, 4, 3, 2]
result = PairSum(nums)
print(result)  


# Question-2

def maxCandies(candyType):
    max_types = len(set(candyType))  
    max_allowed = len(candyType) // 2

    return min(max_types, max_allowed)


candyType = [1, 1, 2, 2, 3, 3]
result = maxCandies(candyType)
print(result) 

# Question-3
def findLHS(nums):
    num_counts = {}
    max_length = 0
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    for num in num_counts:
        if num + 1 in num_counts:
            length = num_counts[num] + num_counts[num + 1]
            max_length = max(max_length, length)
    return max_length

nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)  

#Question-4
def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0

    while i < len(flowerbed):
        if (
            flowerbed[i] == 0 and
            (i == 0 or flowerbed[i - 1] == 0) and
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
        ):
            flowerbed[i] = 1
            count += 1
            i += 1

        if count >= n:
            return True
        i += 1
    return False

flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
print(result) 

#Question-5
def maximumProduct(nums):
    nums.sort() 
    n = len(nums)
    max_product1 = nums[0] * nums[1] * nums[n - 1]
    max_product2 = nums[n - 1] * nums[n - 2] * nums[n - 3]
    return max(max_product1, max_product2)

nums = [1,2,3]
result = maximumProduct(nums)
print(result)  


#Question-6
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [-1,0,3,5,9,12]
target = 9
result = search(nums, target)
print(result)  

#Question-7
def Monotonic(nums):
    increasing = decreasing = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing

nums = [1,2,2,3]
result = Monotonic(nums)
print(result)  

#Question-8
def minimumScore(nums, k):
    nums.sort()  
    min_score = nums[-1] - nums[0]  

    for i in range(1, len(nums)):
        new_min = min(nums[0] + k, nums[i] - k)
        new_max = max(nums[-1] - k, nums[i - 1] + k)
        min_score = min(min_score, new_max - new_min)

    return min_score
nums = [1]
k = 0
result = minimumScore(nums, k)
print(result)



