def count_instances(text, match):
    import re
    count=len([i for i in re.finditer(match,text)])
    return count

text = input('Please provide a text input: ')
match = input('Please provide a word you want to count (case-specific, full words only): ')

print('The word \''+match+'\' in the provided text counts:', str(count_instances(text, match)))
