def ok(b):
    try:
        assert(b)
        print(".", end="", flush=True)
    except:
        print("X", end="", flush=True)
