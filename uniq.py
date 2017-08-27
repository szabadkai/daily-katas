import test


def is_unique(s):
    charset = set()
    for i in s:
        if i in charset:
            return False
        charset.add(i)
    return True


def is_unique_no_new_ds(s):
    return not any((i[1] in s[i[0] + 1:] for i in enumerate(s)))


if __name__ == "__main__":
    test.ok(is_unique("abc"))
    test.ok(is_unique(""))
    test.ok(not is_unique("aa"))
    test.ok(is_unique_no_new_ds("abc"))
    test.ok(is_unique_no_new_ds(""))
    test.ok(not is_unique_no_new_ds("aa"))
    test.ok(not is_unique_no_new_ds("asffff"))
