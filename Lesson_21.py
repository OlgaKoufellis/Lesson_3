# # файлы
#
# # file = open("text.txt", "w")
# # file.write("Your text goes here")
# # file.close()
# # 'r' open for reading (default)
# # 'w' open for writing, truncating the file first
# # 'x' open for exclusive creation, failing if the file already exists
# # 'a' open for writing, appending to the end of the file if it exists
# #
#
#
#
# import time
#
# f = open('test.txt', 'wt')  # t -text b- binary
# f.write('My name is Olga \nHow are you?')
# time.sleep(15)
# f = open('test.txt', 'rt')
# print(f.read())
# f.close()
#
# f = open('test.txt', 'rt')
# print(f.read()) # ситывает файл целиком НЕ БЕЗОПАСЕН
# f.close()
#
# f = open('test.txt', 'rt')
# print(f.readline())
# print(f.readline()) # ситывает файл построчно БЕЗОПАСЕН
# f.close()
#
# f = open('test.txt', 'rt')
# print(f.readlines()) # ситывает файл как список
# f.close()
#
# f = open('test.txt', 'wt')
# f.write('My name is Olga \nHow are you?')
# f.close()
#
# # f = open('test.txt', 'xt') # открыть файл на запись
# # f.write('Hello my dear friend. lets goo outside')
# # f.close()
#
# # + открытие файла на чтение и на запись
# f = open('test1.txt', 'rt+')
# f.write('Hello my dear friend. lets goo outside')
# f.close()



import random
f = open('numbers.txt','wt')
for i in range(10):
    for j in range(10):
        f.write(str(random.randint(1,9)))
    f.write('\n')
f.close()

import random
f = open('numbers2.txt','wt')
for i in range(10):
    for j in range(10):
        f.write(str(random.randint(1,9)))
    f.write('\n')
f.close()


n1 = open('numbers.txt','rt')
n2 = open('numbers2.txt','rt')
n3 = open('numbers3.txt','wt')
ln1 = n1.readline()
ln2 = n2.readline()
while ln1 or ln2:
    n3.write(ln1)
    n3.write(ln2)
    ln1 = n1.readline()
    ln2 = n2.readline()
n3.close()

