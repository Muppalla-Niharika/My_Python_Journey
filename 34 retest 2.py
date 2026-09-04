
s = ""
for i in range(5):
    s = s + "abc"
    print("Loop", i + 1, ":", s)
print("Final string:", s)

#duplicates removed but order isn't correct 
my_list = [10, 20, 20, 30, 10, 40]
unique = set(my_list)
print(unique)

#order is crct and dupicates are removed 
my_list = [10, 20, 20, 30, 10, 40]
unique = list(dict.fromkeys(my_list))
print(unique)

num = (1,2,[3,5,8],9) 
num[2].append(6) 
print(num)

s = "Programming"
result = ""
for ch in s:
    result = ch + result
print(result)


a = [1, 2, 2, 3, 4]
b = [3, 4, 5, 6]
common = set(a) & set(b)
print(common)


def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

s = "hello world"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)