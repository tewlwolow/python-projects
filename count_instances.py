# simple function to count all word instances in a text

from re import finditer


def count_instances(text, match):
    count=len([i for i in finditer(match,text)])
    return count
