def true_if_even(array):
    for index, elem in enumerate(array):
        if elem % 2 == 0:
            return index
        else:
            return -1


def never_true():
    return -1


def true_if_value_equals_index(array):
    for index, value in enumerate(array):
        if int(index) == value:
            return int(index)
        else:
            return -1


def true_if_length_equals_index(array):
    for index, value in enumerate(array):
        if len(value) == index:
            return index
        else:
            return -1


def find_in_array(seq, predicate):
    if predicate == true_if_even:
        return true_if_even(seq)
    elif predicate == never_true:
        return never_true()
    elif predicate == true_if_value_equals_index:
        return true_if_value_equals_index(seq)
    elif predicate == true_if_length_equals_index:
        return true_if_length_equals_index(seq)


print(find_in_array([], true_if_even))
print(find_in_array([1, 3, 5, 6, 7], true_if_even))
print(find_in_array([2, 4, 6, 8], true_if_even))
print(find_in_array([2, 4, 6, 8], never_true))
print(find_in_array([13, 5, 3, 1, 4, 5], true_if_value_equals_index))
print(find_in_array(["one", "two", "three", "four", "five", "six"], true_if_length_equals_index))
print(find_in_array(["bc", "af", "d", "e"], true_if_length_equals_index))
