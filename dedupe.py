

def deduplicate(l: list):
    used_chars = set()
    for i in l:
        if i not in used_chars:
            used_chars.add(i)
            yield i


assert (list(deduplicate(range(1000000))) == list(range(1000000)))
assert (list(deduplicate([1, 2, 3])) == [1, 2, 3])
assert (list(deduplicate([1, 1, 3])) == [1, 3])
assert (list(deduplicate([1, 1, 1])) == [1])
assert (list(deduplicate([])) == [])
print("All passed :)")
