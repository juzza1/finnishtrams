def substr_lists(list1, list2):
    """Substract two lists. Only first occurance in the first list is
    removed."""
    for i in list1[:]:
        if i in list2:
            list1.remove(i)
        else:
            continue
    return list1

def to_list(string):
    """Convert a comma-separated string to a list, remove leading and trailing
    whitespace"""
    list_ = string.split(',')
    return map(str.strip, list_)

def to_int(list_):
    """Convert each element of a list into an integer"""
    return map(int, list_)

def to_upper(list_):
    """Convert each string in a list to uppercase"""
    return map(str.upper, list_)
