# not built in way flatten an array

def flatten(arr, returnArr):
    for i in arr:
        if type(i) is list:
            flatten(i, returnArr)
        else:
            returnArr.append(i)
    return returnArr

assert flatten([[1,2], 3], []) == [1, 2, 3]
assert flatten([[1,2], [3, 4, [5, 6], 7]], []) == [1, 2, 3, 4, 5, 6, 7]