# string compression using a method which counts the characters
# "aaabbbccccaaaab" -> "a3b3c4a3b1"
# if the compressed it not smaller return the original string
# the string has only uppercase and lowercase letters

# the initial thoughts, count the characters as it goes and build a new string
# if the "compressed" string is not smaller, then return the original string

def compress(string):
    new_string = ""
    previous = string[0]
    char_counter = 0


    print(new_string)
    if len(new_string) >= len(string):
        return string
    else:
        return new_string


assert compress("aaabbbccccaaaab") == "a3b3c4a3b1", "error"
assert compress("abc") == "abc", "error"
