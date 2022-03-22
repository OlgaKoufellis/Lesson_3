'''
Задание 1
Реализуйте класс «Человек». Необходимо хранить в полях класса:
ФИО,
дату рождения,
контактный телефон,
город,
страну,
домашний адрес.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''
class Person:

    def __init__(self, name_surname, birthday, telephone_num, city, country, adress):
        self.full_name = name_surname
        self.date_of_birth = birthday
        self.phone_num = telephone_num
        self.city = city
        self.country = country
        self.address = adress

    def short_info_func(self):
        return str(self.full_name + ', ' + self.country + ', ' + self.city)

    def full_info_func(self):
        return str(self.full_name + ', ' + self.date_of_birth + ', ' + self.country + ', ' + self.city + ', ' +
                   self.address + ', ' + self.phone_num)



information_of_a_person = Person(
    'Makar Nevski',
    '12/03/2000',
    '+3598765433',
    'Brovary',
    'Ukraine',
    'Petrovka 23/56b')

print(information_of_a_person.short_info_func())
print(information_of_a_person.full_info_func())


'''
Задание 2 
Создайте класс «Город». 
Необходимо хранить в полях класса: 
-название города, 
-название региона, 
-название страны, 
-количество жителей в городе, 
-почтовый индекс города, 
-телефонный код города. 
Реализуйте методы класса для ввода данных, вывода данных, 
реализуйте доступ к отдельным полям через методы класса.
'''

class City:

    def __init__(self, city_name, region_name, country_name, number_of_citizen, zip_code, code_of_city):
        self.city = city_name
        self.region = region_name
        self.country = country_name
        self.citizen = number_of_citizen
        self.zip = zip_code
        self.code = code_of_city

    def short_info(self):
        return str('country is :' + self.country +' ' + 'and zip code is :' + self.zip )

    def full_info(self):
        return str(self.zip +' ' + self.country  +' ' + self.region +' ' + self.city +' ' +'Code :' +' ' + self.code +' ' +
                   'Number of citizenship :' +' ' + self.citizen)

first_city = City(
    'Bansko',
    'Bansko',
    'Bolgaria',
    '12 774',
    '2770',
    '+359'
)

second_city = City(
    'Bila Tserkva',
    'Kyiv',
    'Ukraine',
    '203 816',
    '09100',
    '+380'
)

print(first_city.full_info())
print(second_city.full_info())

print(first_city.short_info())
print(second_city.short_info())

'''
Задание 3 
Создайте класс «Страна». 
Необходимо хранить в полях класса: 
-название страны, 
-название континента, 
-количество жителей в стране, 
-телефонный код страны, 
-название столицы, 
-название городов страны. 
Реализуйте методы класса для ввода данных, вывода данных, 
реализуйте доступ к отдельным полям через методы класса.
'''

class Country:
    cities_name = []
    capital = ''
    phone_code = ''
    number_of_citizen = ''
    mainland = ''
    country_name = ''


    def __init__(self, city, capital_, phone, citizen, mainland_, country):
        self.cities_name = city
        self.capital = capital_
        self.phone_code = phone
        self.number_of_citizen = citizen
        self.mainland = mainland_
        self.country_name = country

    def some_info(self):
        return self.capital,self.mainland, self.country_name

    def all_the_info(self):
        return self.cities_name, self.capital, self.phone_code, self.number_of_citizen, self.mainland, self.country_name

    def number_of_citizen(self, new_number_of_citizen):
        self.number_of_citizen = new_number_of_citizen
    def new_number_of_citizen(self):
        return self.number_of_citizen


Ukraine_Country = Country(
    ['Kyiv', 'Kharkov', 'Odessa', 'Lviv', 'Rivne', 'Bila Tserkva', 'Mariupol', 'Dnipro', 'Nikolaev'],
    'Kyiv',
    '00380...',
    '250 000',
    'Europe',
    'Ukraine',
)
Bolgaria_Country = Country(
    ['Sofia', 'Bansko', 'Razlog', 'Blagoevgrad', 'Varna'],
    'Sofia',
    '00359...',
    '1 674 651',
    'Europe',
    'Bolgaria',
)


print(Ukraine_Country.some_info())
print(Ukraine_Country.all_the_info())

print(Bolgaria_Country.all_the_info())
print(Bolgaria_Country.some_info())

Bolgaria_Country.number_of_citizen = '1234567890'
print(Bolgaria_Country.new_number_of_citizen())


######### II ##########


# class Country:
#     country_name = ''
#     mainland = ''
#     number_of_citizen = ''
#     phone_code = ''
#     capital = ''
#     cities_name = []
#
#     def all_the_info (self, city, capital_, phone, citizen, mainland_, country):
#         self.cities_name = city
#         self.capital = capital_
#         self.phone_code = phone
#         self.number_of_citizen = citizen
#         self.mainland = mainland_
#         self.country_name = country
#         return self.cities_name , self.capital, self.phone_code, self.number_of_citizen, self.mainland, self.country_name
#
#     def some_info (self, capital_, mainland_, country):
#         self.capital = capital_
#         self.mainland = mainland_
#         self.country_name = country
#         return self.capital,self.mainland, self.country_name
#
# Ukraine_Country = Country()
# Bolgaria_Country = Country()
#
#
# print(Ukraine_Country.all_the_info(
#     ['Kyiv', 'Kharkov', 'Odessa', 'Lviv', 'Rivne', 'Bila Tserkva', 'Mariupol', 'Dnipro', 'Nikolaev'],
#     'Kyiv',
#     '00380...',
#     '250 000',
#     'Europe',
#     'Ukraine',
# ))
#
# print(Bolgaria_Country.all_the_info(
#     ['Sofia', 'Bansko', 'Razlog', 'Blagoevgrad', 'Varna'],
#     'Sofia',
#     '00359...',
#     '1 674 651',
#     'Europe',
#     'Bolgaria',
# ))
#
# print(Ukraine_Country.some_info(
#     'Kyiv',
#     'Europe',
#     'Ukraine',
# ))

'''
Задание 4 
Создайте класс «Дробь». 
Необходимо хранить в полях класса: числитель и знаменатель. 
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 
Также создайте методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).
'''

class Fraction:

    def __init__(self, number_1, number_2):
        self.first_number = number_1
        self.second_number = number_2



    def result(self, sign):
        if sign == '/':
           res = self.first_number / self.second_number
        if sign == '*':
            res = self.first_number * self.second_number
        if sign == '+':
            res = self.first_number + self.second_number
        if sign == '-':
            res = self.first_number - self.second_number
        if sign == '**':
            res = self.first_number ** self.second_number
        return res



first_fraction = Fraction (2, 5)
second_fraction = Fraction (125, 45)
print(first_fraction.result('*'))
print(first_fraction.result('/'))
print(first_fraction.result('+'))
print(first_fraction.result('-'))
print(first_fraction.result('**'))

print(second_fraction.result('*'))
print(second_fraction.result('/'))
print(second_fraction.result('+'))
print(second_fraction.result('-'))



