# Задача 21
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text='мы вкл детскую программу и начали учить алфавит с букв абвгд, а потом стали смотреть абвгдейку'
print(my_text)
print(' '.join(filter(lambda y: not 'абв' in y, my_text.split())))

# print(s for s in my_text.split() if not 'абв' in my_text)

# print(list(filter(word for word in my_text.split() if not 'абв' in word)))

# print(my_text)
# range_of_words=my_text.split()
# for i in range_of_words:
#     if 'абв' in i:
#         range_of_words.remove(i)
# print(' '.join(range_of_words))

