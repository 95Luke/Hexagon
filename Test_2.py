#!/bin/python3

import os
import platform
import sys


##
# @brief    function that allows cross-platform usage of program, determines type of separator
#           that should be used
#
# @return   slash_separator - separator appropriate to the platform
#
def set_separator():
    slash_separator = ''

    if platform.system() == 'Windows':
        slash_separator = '\\'
    elif platform.system() in ('Linux', 'Darwin'):
        slash_separator = '/'
    else:
        print('Unknown system')
        exit(1)
    return slash_separator


##
# @brief    uses os.walk to recrusively search for files and creates list of tuples
#           containing accordingly size in bytes and file name
#
# @param    search_dir - directory that will be used for search                 (str)
#
# @return   files_list - a list containing tuples with size and file names      (list(tuple)) 
#
def search_and_create_files_list(search_dir):
    files_list = []
    separator = set_separator()

    for dirpath, dirnames, filenames in os.walk(search_dir):
        for name in filenames:
            file_size =  os.stat(dirpath + separator + name).st_size
            files_list.append((file_size, name))

    files_list.sort(key=lambda values: values[1])

    return files_list


##
# @brief    calls seatch_and_create_files_list function and utilizes values to create
#           sorted dictionary with keys from the first 3 letters of a name
#
# @param    walk_dir - directory that will be used for search                   (str)
#
# @return   dictionary - dict containing first 3 letters as key and list of
#           tuples sorted by size as values                                     (dict)
#
def create_dictionary(walk_dir):
    dictionary = {}
    files = search_and_create_files_list(walk_dir)

    for element in files:
        file_name = element[1]
        dict_key = file_name[:3]

        if dict_key not in dictionary:
            dictionary[dict_key] = [element]
        else:
            dictionary[dict_key].append(element)

    for dict_key in dictionary:
        dictionary[dict_key].sort(key=lambda values: values[0], reverse=True)

    return dictionary


if __name__ == '__main__':
    ### TO-DO - create function verifying if the input is correct, unfortunately I did not have
    #           enough time to do it & create sufficient UT to test it
    #
    scan_dir = sys.argv[1]
    print(create_dictionary(scan_dir))

