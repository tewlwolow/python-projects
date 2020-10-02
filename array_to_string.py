# simple function to convert list/tuple elements into a natural string (with Oxford commas)


def array_to_string(array):
    try:
        if len(array)==1:
            return str(array[0])
        else:
            return('{}, and {}'.format(', '.join(map(str, array[:-1])), str(array[-1])))
    except (IndexError):
        return('Your list is empty.')
