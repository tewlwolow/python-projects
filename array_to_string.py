# simple function to convert list/tuple elements into a natural string (with Oxford commas)


def array_to_string(array):
    try:
        if len(array)==1:
            return array
        else:
            return ('{}, and {}'.format(', '.join(map(str, array[:-1])), str(array[-1])))
    except (IndexError):
        print('Your list is empty.')
