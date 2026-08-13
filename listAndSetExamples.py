def missing_numbers(nums,n):
    present = set(nums)
    return [x for x in range(1,n+1) if x not in present]

nums = [1, 2, 4, 6, 7]
missing = missing_numbers(nums, 10)
print("Missing numbers:", missing)

def symmetric_difference_ordered(a, b):
    only_one = set(a).symmetric_difference(set(b))
    combined = a + b
    result = []
    for item in combined:
        if item in only_one and item not in result:
            result.append(item)
    return result

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
sym_diff = symmetric_difference_ordered(a, b)
print("Symmetric difference (ordered):", sym_diff)


def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is greater than the length of the list
    return lst[-k:] + lst[:-k]

rotated_list = rotate_list([1, 2, 3, 4, 5], 6)
print("Rotated list:", rotated_list)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

nested_list = [[1, 2], [3, 4], [5]]
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

def length_bucket_loop(sentence: str) ->list[list[str]]:
    words = sentence.split()
    if not words:
        return []
    
    max_len = max(len(w) for w in words)
    buckets = [[] for _ in range(max_len)]

    for w in words:
        buckets[len(w) - 1].append(w)
    
    return buckets

sentence = "to be or not to be that is the question"
length_buckets = length_bucket_loop(sentence)
print("Length buckets:", length_buckets)

def count_duplicates(data):
    seen = set()
    duplicates = set()
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return len(duplicates)

print("Count of duplicates:", count_duplicates([1, 2, 3, 2, 4, 5, 1, 6]))