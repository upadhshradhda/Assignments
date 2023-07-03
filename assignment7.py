# Question-1
def isomorphic(s, t):
    if len(s) != len(t):
        return False
    char_map = {}
    mapped_chars = set()
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s in char_map:
            if char_map[char_s] != char_t:
                return False
        else:
            if char_t in mapped_chars:
                return False
            char_map[char_s] = char_t
            mapped_chars.add(char_t)
    return True

s1 = "egg"
t1 = "add"
print(isomorphic(s1,t1))  


# Question-2
def strobogrammatic(num):
    strob_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1
    while left <= right:
        if num[left] not in strob_map or strob_map[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    return True

num1 = "69"
print(strobogrammatic(num1))  


# Question-3
def add(num1, num2):
    carry = 0
    result = []
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0 or carry:
        digit_sum = carry
        if i >= 0:
            digit_sum += int(num1[i])
            i -= 1
        if j >= 0:
            digit_sum += int(num2[j])
            j -= 1
        carry = digit_sum // 10
        digit = digit_sum % 10
        result.append(str(digit))
    return ''.join(result[::-1])

num1 = "11"
num2 = "123"
print(add(num1,num2))  


#Question-4
def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

sentence = "Let's take LeetCode contest"
print(reverse_words(sentence))  


# Question-5
def reverse_str(s, k):
    result = ""
    i = 0
    while i < len(s):
        if i + k <= len(s):
            result += s[i:i+k][::-1]
        else:
            result += s[i:][::-1]
        if i + 2*k <= len(s):
            result += s[i+k:i+2*k]
        else:
            result += s[i+k:]
        i += 2*k
    return result

s1 = "abcdefg"
k1 = 2
print(reverse_str(s1,k1))  


# Question-6
def shift(s, goal):
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        shifted = s[i:] + s[:i]
        if shifted == goal:
            return True
    return False

s = "abcde"
goal = "bcdea"
print(shift(s,goal))


# Question-7
def equal(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    return process_string(s) == process_string(t)

s1 = "ab#c"
t1 = "ad#c"
print(equal(s1,t1)) 


# Question-8
def straight_line(coordinates):
    if len(coordinates) <= 2:
        return True
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x0) * (y1 - y0) != (x1 - x0) * (y - y0):
            return False
    return True

coordinates1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(straight_line(coordinates1))  


