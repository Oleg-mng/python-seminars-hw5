# Задача 24
#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaffffcc
# a3f4c2

def rle_code(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            encoding += prev_char+str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += prev_char+str(count)
    return encoding
var_1='aaaffffcc'
with open('file24.enter.txt', 'w') as data:
    data.write(var_1)
with open('file24.enter.txt', 'r') as f:
    enter = f.read()

new_val_rle = rle_code(enter)
print(new_val_rle)

with open('file24.exit.txt', 'w') as data:
    data.write(new_val_rle)
