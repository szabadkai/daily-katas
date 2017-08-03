from collections import Counter
from memory_profiler import profile

@profile
def is_all_uniq(text: str):
    return not any((i > 1 for i in Counter(text).values()))

@profile
def is_all_uniq_no_ds(text: str):
    for i, l in enumerate(text):
        if l in text[i+1:]:
            return False
    return True

import dis
import random
import string
print(dis.dis(is_all_uniq))
print(dis.dis(is_all_uniq_no_ds))

test_string=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1000000))



assert(is_all_uniq("helo") is True)
assert(is_all_uniq("false") is True)
assert(is_all_uniq("hello") is False)
assert(is_all_uniq(test_string) is False)

assert(is_all_uniq_no_ds("helo") is True)
assert(is_all_uniq_no_ds("false") is True)
assert(is_all_uniq_no_ds("hello") is False)
assert(is_all_uniq_no_ds(test_string) is False)
