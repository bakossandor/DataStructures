# write a function using iteration to reverse a string
# after reverse a string using recursion

# these are the basics
# of course there are the python built ins like [::-1] and reverse list method

def reverse_it(string):
    reversed_s = ""
    for char in string:
        reversed_s = char + reversed_s
    return reversed_s


assert reverse_it("string") == "gnirts", "error"
assert reverse_it("dadda") == "addad", "error"
assert reverse_it("Hello my friend!") == "!dneirf ym olleH", "error"


def reverse_recursevly(string):
    if len(string) == 1:
        return string
    return reverse_recursevly(string[1:]) + string[0]

assert reverse_recursevly("string") == "gnirts", "error"
assert reverse_recursevly("dadda") == "addad", "error"
assert reverse_recursevly("Hello my friend!") == "!dneirf ym olleH", "error"


def reverse_with_build_ins(string):
    new_list = list(string)
    new_list.reverse()
    return_this = "".join(new_list)
    return return_this

assert reverse_with_build_ins("string") == "gnirts", "error"
assert reverse_with_build_ins("dadda") == "addad", "error"
assert reverse_with_build_ins("Hello my friend!") == "!dneirf ym olleH", "error"