import sys
import unicodedata

def is_nfd(line):
    for char in line.strip():
        if unicodedata.combining(char) != 0:
            return True
    return False

def show_unicode_name(line):
    for char in line.strip():
        name = unicodedata.name(char)
        space = ' '
        if unicodedata.combining(char) != 0:
            space += ' '
        print(f'{char}{space}: {name}')

filename = sys.argv[1]
with open(filename, encoding='utf-8') as f:
    for line in f:
        text = [char for char in line.strip()]
        print(f'文字単位: {text}, 長さ: {len(text)}')
        show_unicode_name(line)

        if is_nfd(line):
            print('NFD から NFC への変換')
            converted = unicodedata.normalize('NFC', line)
            show_unicode_name(converted)
