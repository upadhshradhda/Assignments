# Question-1

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum == target:
                return target

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum > target:
                right -= 1
            else:
                left += 1

    return closestSum


nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))


# Question-2

def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]
                if currentSum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

    return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))


# Question-3
def nextPermutation(nums):
    n = len(nums)

    # Step 1: Find the first index `i` from the right where `nums[i]` is less than its adjacent element
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the first index `j` from the right where `nums[j]` is greater than `nums[i]`
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap the elements at indices `i` and `j`
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the subarray from index `i + 1` to the end
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
nums = [1, 2, 3]
print(nextPermutation(nums))


# Question-4
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))

# Question-5
def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry

        if digits[i] < 10:
            return digits

        digits[i] = 0
        carry = 1

    digits.insert(0, 1)
    return digits
digits = [1, 2, 3]
print(plusOne(digits))


# Question-6
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
nums = [2, 2, 1]
print(singleNumber(nums))


# Question-7
def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num == start:
            start += 1
        elif num > start:
            result.append(getRange(start, num - 1))
            start = num + 1

    if start <= upper:
        result.append(getRange(start, upper))

    return result

def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return [str(start) + ', '+ str(end)]

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))


# Question-8
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))
