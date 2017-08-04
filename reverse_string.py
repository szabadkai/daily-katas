

def reverse_c_string(word: str):
    return word[-2::-1]+"\0"


assert(reverse_c_string("hola\0") == "aloh\0")
assert(reverse_c_string("\0") == "\0")
assert(reverse_c_string("ibi\0") == "ibi\0")
