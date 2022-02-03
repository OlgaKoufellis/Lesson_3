#tuple / dict
# tuple картеж (масив) - используется для гарантированной передачи чегото
# не изменяемый список  может все тже самое что и списокб записать отрезать - нельзя
# tuple = () ,
#dict = {}
#list =[]

# tuple / dict
# list = [] список
# tuple = (,) кортеж
# dict = {} словарь
# tuple кортеж (массив)
# #итерируемый тип данных\ не изменяемый тип данных\ индексируемый
# не изменяемый список
bucket = ('Tomato', 'Bread', 'Butter')
# a = 2
# b = 3
# a,b = b,a
# print(a,b)
a = [1, 2, 3]
b = [2]
c = [3]
trio = (a, b, c)
print(trio)
a[0] = 10
a.append(2)
b[0] = 22
c[0] = 0
print(trio)

# dict словарь (массив)
# #итерируемый тип данных\ изменяемый тип данных\ ключ значение \не упорядоченый в памяти
countries = {'Ukraine': 'Kiev', 'Poland': 'Warshava'}
d = {0: 'Andrey', 'a': 'Forever', 'k': 3}
#ключ - любой неизменяемый тип данных : значение - любой тип данных
print(d)
print(d['a'])
d['a'] = 'Never'
print(d)
d['a'] = ['Never','Forever']
print(d)
print(d['a'][0])
d['b'] = 'abc'#Add new element
print(d)
d.pop('k')#Delete by key and pop it
print(d)
print(d.popitem())#Delete random and pop it
print(d)
'''dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, 
возвращает default (по умолчанию бросает исключение).
dict.popitem() - удаляет и возвращает пару (ключ, значение). 
Если словарь пуст, бросает исключение KeyError. 
Помните, что словари неупорядочены.'''
print(d.keys())
print(d.values())




bucket =('Tomato', 'Bread', 'Butter')
bucket[0]
a = 2
b = 3
a,b = b, a
print(a,b)

a = [1, 2, 3]
b = [2]
c = [3]

trio = (a,b,c)
print(trio)
a[0] = 10
b[0] = 22
c[0] = 0
print(trio)




#CRUD
#C - Create
#R - Read
#U - Update
#D - Delete
notes = {}
#C - Create
title = str(input("Enter name of your note : "))#key
note = str(input("Enter text of your note : "))#value
notes[title] = note
print(notes)
#U - Update
title = str(input("Enter name of your note : "))#key
note = str(input("Enter text of your note : "))#value
notes[title] = note
print(notes)



