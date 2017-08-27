class Hash:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [[] for i in range(table_size)]

    def hashf(self, item):
        return sum([ord(i) for i in str(item)]) % self.table_size

    def __setitem__(self, key, value):
        for pair in self.table[self.hashf(key)]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[self.hashf(key)].append([key, value])

    def __getitem__(self, item):
        for pair in self.table[self.hashf(item)]:
            if pair[0] == item:
                return pair[1]
        raise KeyError("No such key {}".format(item))


if __name__ == "__main__":
    import test

    dic = Hash()
    dic[1] = 2
    test.ok(dic[1] == 2)

    dic[1] = 5
    dic[11] = 3

    test.ok(dic[1] == 5)
    test.ok(dic[11] == 3)

    try:
        dic[12]
    except KeyError as e:
        test.ok(e.args[0] == "No such key 12")
