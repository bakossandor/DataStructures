# write a method to replace all space in a string with '%20'

# first thoughts
# use an additional data structure to store the elements
# iterate over the characters

def replace(string):
    new_string = ""
    for char in string:
        if char == " ":
            new_string = new_string + "%20"
        else:
            new_string = new_string + char
    return new_string


assert replace("This is an example") == "This%20is%20an%20example", 'error'
assert replace("Space here") == "Space%20here"
