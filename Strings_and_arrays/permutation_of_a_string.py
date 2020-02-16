# check if two strings are permutation of the others
# - case sensitive - so "Dog" is not permutation of "dog"
# - whitespace is matters - so "dog   " is not permutation of "dog"

def isPermutation(a, b):
    if "".join(sorted(a)) == "".join(sorted(b)):
        return True
    return False


assert isPermutation("word", "dorw") is True, "error"
assert isPermutation("word", "doesnotmatch") is False, "error"
assert isPermutation("abcde edaed", "abcdeedaed") is False, "error"
assert isPermutation("A", "a") is False, "error"