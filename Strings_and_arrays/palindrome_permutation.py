# given a string, write a function to check if it is a permutation a of a palindorme

# input Tact Coa
# output True (permutations: "taco cat", "atco cta", etc.

# firts implementation
# remove whitespace
# check the length of the string
# we need pairs
# if the length is even we need full pairs
# if the lenght is odd we need full pairs + one extra char
# we need make the uppercase all as well

def check_if_it_is_a_palindrome_mutation(string):
    # trim the words
    trimmed = "".join(string.split(" "))
    upperAll = trimmed.upper()
    length = len(trimmed)
    dictionary = {}
    for char in upperAll:
        if (char in dictionary) is False:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    odds = 0
    for key in dictionary:
        if dictionary[key] %2 == 1:
            odds += 1
    if odds > 1:
        return False
    if odds == 1 and length % 2 == 0:
        return False
    else:
        return True



assert check_if_it_is_a_palindrome_mutation("Tact Coa") is True, "error"
assert check_if_it_is_a_palindrome_mutation("Sinononis") is True, "error"
assert check_if_it_is_a_palindrome_mutation("This is no a palindrome mutation") is False, "error"
