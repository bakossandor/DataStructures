# Implement a algorithm to determine if a string has all unique characters.
# What if you can't use additional data structures?

# Clarify the problem
# inputs
# "unique" -> false (the "u" character included twice)
# "one" -> true (all characters has seen only once)

# solution one is bruteforce
# go character by character and see if the character is unique by check against all of the other character
# an optimized version of the bruteforce is hcekc against all of the remaining characters because the "current" character has been tested once before with the previous characters so they are obviously does not match

# we have to emphasize if we can use like an "other" data structure we would use the hash table, or binary tree

def unique(string):
    for char in range(0, len(string)):
        for compare_char in range(char + 1, len(string)):
            if (string[char] == string[compare_char]):
                return False
    return True


assert unique("unique") is False, "we have a problem"
assert unique("one") is True, "we have a problem"
assert unique("one1") is True, "we have a problem"
assert unique("11") is False, "we have a problem"


# using other data structure

def unique2(string):
    lookup = {}
    for char in string:
        if lookup.get(char) is True:
            return False
        else:
            lookup[char] = True
    return True

assert unique2("unique") is False, "we have a problem"
assert unique2("one") is True, "we have a problem"
assert unique2("one1") is True, "we have a problem"
assert unique2("11") is False, "we have a problem"