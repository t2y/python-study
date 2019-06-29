import sys
import unicodedata

def show_unicode_name(line):
    for char in line.strip():
        name = unicodedata.name(char)
        space = ' '
        if unicodedata.combining(char) != 0:
            space += ' '
            is_nfd = True
        print(f'{char}{space}: {name}')

filename = sys.argv[1]
with open(filename, encoding='utf-8') as f:
    for line in f:
        text = [char for char in line.strip()]
        print(f'文字単位: {text}, 長さ: {len(text)}')
        show_unicode_name(line)
