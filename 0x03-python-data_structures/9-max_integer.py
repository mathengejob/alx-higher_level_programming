def max_integer(my_list=[]):
    max_ = 0
    for number in my_list:
        if number > max_:
            max_ = number
    return max_
