def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    max_ = my_list[0]
    for i in my_list:
        if i > max_:
            max_ = i
    return max_
