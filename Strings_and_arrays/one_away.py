# There are three types of edits that can be performed on a srtings: insert a character, remove a character, or replace a character.
# Givent two strings, write a function to check if they are on edit (or zero edit) away

# pale, ple -> true
# pales, pale -> true

# first thoughts - we really need to seperate the cases
# the most easiest cas if the length of the string is the same
# if the length is plus minus 1 we can use an other function to identify the problem
# which utilize pointers based on the indexes - and allow one one comparision failiure
# like
# "abc" pointers 0-a, 1-b, 2-c
# "adbc" pointers 0-a, 1-d, 2-b, 3-c --> and here we are going to increase the pointer with one


def compare_same_len(s1, s2):
    mismatch = False
    for idx in range(0, len(s1)):
        if s1[idx] != s2[idx]:
            if mismatch is True:
                return False
            mismatch = True
    return True


def compare_not_same_len(longer, shorter):
    # run a loop until the shorter ends
    idx1 = 0
    idx2 = 0
    while idx2 + 1 != len(shorter):
        if longer[idx1] != shorter[idx2]:
            if idx1 != idx2:
                return False
            idx1 += 1
        idx1 += 1
        idx2 += 1
    return True


def one_away(string1, string2):
    if string1 == string2:
        return True
    elif len(string1) == len(string2):
        return compare_same_len(string1, string2)
    elif len(string1) - len(string2) == 1:
        return compare_not_same_len(string1, string2)
    elif len(string1) - len(string2) == -1:
        return compare_not_same_len(string2, string1)
    else:
        return False

assert one_away("one", "one") is True, "error"
assert one_away("not", "one away") is False, "error"
assert one_away("pig", "dig") is True, "error"
assert one_away("one", "on") is True, "error"
assert one_away("this", "thisi") is True, "error"
assert one_away("pig", "dii") is False, "error"