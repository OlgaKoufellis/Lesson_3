'''
Задание 1

К уже реализованному классу «Автомобиль» добавьте конструктор, а также необходимые перегруженные методы.
'''
class Car:
    _model = "Octavia"
    year_of_issue = 2022
    __manufacturer = "Ukraine"
    engine_capacity = "3,2"
    color = "black"
    price = 15000

    def __init__(self, year_of_issue, color, price):
        self.year_of_issue = year_of_issue
        self.color = color
        self.price = price

    def __str__(self):
        return f'Price is : {self.price}\nColor : {self.color}\nYear of issue is: {self.year_of_issue}'

    def __add__(self, other):
       self.price = self.price + other.price

    def __int__(self):
        print("NOT INT")

    def year_OF_issue(self):
        print(self.year_of_issue)

    def new_color(self, new_color):
        self.color = new_color

    def new_model(self, new_model='KALINA'):
        self._model = new_model

    def car_price(self, year):
        new_price = 3000
        if year == 2000:
            self.price = new_price + 1000
        if year == 2002:
            self.price = new_price + 2200
        if year == 2005:
            self.price = new_price + 3700
        if year == 2010:
            self.price = new_price + 5000
        if year == 2015:
            self.price = new_price + 7500
        if year == 2020:
            self.price = new_price + 12000
        return self.price

shkoda_octavia = Car(2000, 'blue_yellow', 25000)
print(shkoda_octavia.year_of_issue)

print(shkoda_octavia.price)
print(shkoda_octavia.color)
print(shkoda_octavia._model)

print(shkoda_octavia)

mercedes_octavia = Car(2023, 'pearl-pink', 100000)
mercedes_octavia.new_model('mercedes-octavia')
print(mercedes_octavia._model)
print(mercedes_octavia)
mercedes_octavia + shkoda_octavia
print(mercedes_octavia.price)
mercedes_octavia + shkoda_octavia
print(mercedes_octavia.price)



# shkoda_octavia.year_of_issue = 2005
# # print(shkoda_octavia.year_of_issue)
# shkoda_octavia.year_OF_issue()
#
# print(shkoda_octavia.price)
#
# print(shkoda_octavia.car_price(2005))
# print(shkoda_octavia.price)
#
#
# Zhyguli_octavia = Car()
#
# print('Our car is Zhyguli Octavia',
#       '\nmodel is:', Zhyguli_octavia._model ,
#       '\nprice is: ',Zhyguli_octavia.price,
#       '\ncolor is: ',Zhyguli_octavia.color,
#       '\nyear of issue:',Zhyguli_octavia.year_of_issue,
#       '\nengine capacity is:',Zhyguli_octavia.engine_capacity)
#
# print(Zhyguli_octavia.price)
# print('year of issue:' ,Zhyguli_octavia.year_of_issue)
# Zhyguli_octavia.car_price(2000)
# print('price is: ', Zhyguli_octavia.price)
#
# Zhyguli_octavia.new_color('Gold')
# print('color is: ', Zhyguli_octavia.color)
#
# print(Zhyguli_octavia._model)
# Zhyguli_octavia.new_model()
# print(Zhyguli_octavia._model)
#
# Zhyguli_octavia.year_of_issue = 2000
# Zhyguli_octavia.year_OF_issue()
#
# print('Our car is Zhyguli Octavia',
#       '\nmodel is:', Zhyguli_octavia._model ,
#       '\nprice is: ',Zhyguli_octavia.price,
#       '\ncolor is: ',Zhyguli_octavia.color,
#       '\nyear of issue:',Zhyguli_octavia.year_of_issue,
#       '\nengine capacity is:',Zhyguli_octavia.engine_capacity)


'''
Задание 2

К уже реализованному классу «Книга» добавьте конструктор, а также необходимые перегруженные методы.
'''

class Book:
    name = ''
    date_of_issue = 2022
    _publisher = 'Knizhniy_klub'
    style = ''
    author = "Bandera_Stepan"
    price = 100

    def __init__(self, name, date_of_issue, style):
        self.name = name
        self.date_of_issue = date_of_issue
        self.style = style

    def __str__(self):
        return f'Name of the book: {self.name}\nDate of issue : {self.date_of_issue} \nStyle is: {self.style}'

    def __add__(self, other):
        self.price = self.price + (20 * self.price )/100

    def book_name(self, new_name):
        self.name = new_name
        return self.name

    def book_style(self, style_book = "Classics"):
        if style_book == "Classics":
            self.new_style("Classics")
        elif style_book == "Action":
            self.new_style("Action")
        elif style_book == "Horror":
            self.new_style("Horror")
        elif style_book == "Fantasy":
            self.new_style("Fantasy")
        return style_book

    def new_style(self, param):
        self.style = param
        return self.style

    def book_price(self):
        new_price = 0
        if self.style == "Classics":
            new_price = self.price + self.price / 10
        elif self.style == "Action":
            new_price = self.price + self.price / 15
        elif self.style == "Horror":
            new_price = self.price + self.price / 20
        elif self.style == "Fantasy":
            new_price = self.price + self.price / 50
        return new_price


The_Da_Vinci_Code = Book('The_Da_Vinci_Code', 2000,"Horror")

print(The_Da_Vinci_Code.name)
print(The_Da_Vinci_Code.date_of_issue)
print(The_Da_Vinci_Code.style)

print(The_Da_Vinci_Code)

The_Da_Vinci_Code + The_Da_Vinci_Code
print(The_Da_Vinci_Code.price)

Mr_Bin = Book('Mr_Bin:Love_me', 2018,"Fantasy")
print(Mr_Bin.name)
print(Mr_Bin.date_of_issue)
print(Mr_Bin.style)

print(Mr_Bin)
Mr_Bin +Mr_Bin
print(Mr_Bin.price)


# The_Da_Vinci_Code = Book()
#
# The_Da_Vinci_Code.name = 'The_Da_Vinci_Code'
# print('The book name is:', The_Da_Vinci_Code.name)
#
# print(The_Da_Vinci_Code.date_of_issue)
#
# The_Da_Vinci_Code.book_style()
#
# The_Da_Vinci_Code.book_style("Horror")
#
# The_Da_Vinci_Code.book_price()
# print(The_Da_Vinci_Code.book_price())
#
# The_Da_Vinci_Code.book_style("Fantasy")
#
# print(The_Da_Vinci_Code.style)
# The_Da_Vinci_Code.book_price()
# print(The_Da_Vinci_Code.book_price())
# print(The_Da_Vinci_Code.date_of_issue,","
#       ,'the price is:', The_Da_Vinci_Code.book_price(),
#       ",", The_Da_Vinci_Code.name,
#       ",","Author:", The_Da_Vinci_Code.author)

'''
Задание 3

К уже реализованному классу «Стадион» добавьте конструктор, а также необходимые перегруженные методы.
'''
class Stadium:
    name = ''
    opening_date = '24.02.2022'
    country = " "
    city = " "
    capacity = 1000

    def __init__(self, name, country, city):
        self.name = name
        self.country = country
        self.city = city

    def __str__(self):
        return f'The name of the  stadium is: {self.name} \nCounty : {self.country} \nCity name: {self.city}'

    def __add__(self, other):
        self.capacity = self.capacity + other.capacity


    def stadium_name(self, param):
        self.name = param
        return self.name

    def stadium_country(self, param):
        self.country = param
        return self.country

    def stadium_city(self, param):
        self.city = param
        return self.city

    def add_PEOPLE(self):
        self.capacity = self.capacity + 50
        return self.capacity

    def change_date(self, new_date):
        self.opening_date = new_date
        return new_date

Dinamo = Stadium('Dinamo', 'Ukraine', 'Odessa' )
print(Dinamo.name)
print(Dinamo.country)
print(Dinamo.city)

print(Dinamo)

# Dinamo = Stadium()
#
# Dinamo.stadium_name('Dinamo')
# print(Dinamo.name)
#
# print("opening date is:", Dinamo.opening_date)
#
# Dinamo.stadium_country("Ukraine")
# print(Dinamo.country)
#
# Dinamo.stadium_city("Odessa")
# print(Dinamo.city)
#
# Dinamo.add_PEOPLE()
# print(Dinamo.capacity)
# Dinamo.add_PEOPLE()
# print(Dinamo.capacity)
# Dinamo.add_PEOPLE()
# print(Dinamo.capacity)
#
Azov = Stadium('Azov','USA','Arizona')
print(Azov.name)
print(Azov.country)
print(Azov.city)

print(Azov)

Azov + Dinamo
print(Azov.capacity)
Azov + Dinamo
print(Azov.capacity)
Azov + Dinamo
print(Azov.capacity)


# Azov = Stadium()
# Azov.stadium_name("Azov")
# print(Azov.name)
#
# print("opening date is:", Azov.opening_date)
#
# Azov.add_PEOPLE()
# print(Azov.capacity)
# Azov.add_PEOPLE()
# print(Azov.capacity)
#
# Azov.change_date("01.04.2022")
# print("opening date is:", Azov.opening_date)
