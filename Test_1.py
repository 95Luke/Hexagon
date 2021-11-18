#!/usr/bin/python3

a = ['century', 'customer', 'democratic', 'Congress', 'customer', 'evening',
     'often', 'outside', 'reveal', 'weight', 'western', 'century']

b = ['weapon', 'western', 'traditional', 'guess', 'customer', 'exist',
     'democratic', 'Congress', 'evening', 'finish', 'western', 'executive']

##
# @brief    creates a list sorted by length and alphabetically of unique elements created
#           from two passed lists
#
# @param    list_1 - first list containing data                         (list)
# @param    list_2 - second list containing data                        (list)
#
# @return   new_list - list containing combined, unique data            (list)
#
def create_common_list(list_1, list_2):
    if verify_arguments(list_1, list_2) is False:
        exit(1)

    new_list = sorted(list(set(list_1 + list_2)), key=lambda item: (len(item), item))
    return new_list


##
# @brief    function that verifires if provided arguments are lists
#
# @param    arg_1 - fisrt argument to check                             (list)
# @param    arg_2 - second argument to check                            (list)
#
# @return   True if they are both lists, False in other case            (bool)
#
def verify_arguments(arg_1, arg_2):
    if not isinstance(arg_1, list) or not isinstance(arg_2, list):
        return False
    return True


if __name__ == '__main__':
    result = create_common_list(a, b)
    print(result)
    verify_arguments(a, b)

