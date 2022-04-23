'''
Задание 1
Реализуйте класс «Автомобиль».
Необходимо хранить в полях класса:
название модели, год выпуска,
производителя,
объем двигателя,
цвет машины,
цену.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

'''


class Car:
    _model = "Octavia"
    year_of_issue = 2022
    __manufacturer = "Ukraine"
    engine_capacity = "3,2"
    color = "black"
    price = 15000

    def year_OF_issue(self):
        print(self.year_of_issue)

    def new_color(self, new_color):
        self.color = new_color

    def new_model(self):
        self._model = "KALINA"

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

shkoda_octavia = Car()
print(shkoda_octavia._model)

shkoda_octavia.year_of_issue = 2005
# print(shkoda_octavia.year_of_issue)
shkoda_octavia.year_OF_issue()

print(shkoda_octavia.price)

print(shkoda_octavia.car_price(2005))
print(shkoda_octavia.price)


Zhyguli_octavia = Car()

print('Our car is Zhyguli Octavia',
      '\nmodel is:', Zhyguli_octavia._model ,
      '\nprice is: ',Zhyguli_octavia.price,
      '\ncolor is: ',Zhyguli_octavia.color,
      '\nyear of issue:',Zhyguli_octavia.year_of_issue,
      '\nengine capacity is:',Zhyguli_octavia.engine_capacity)

print(Zhyguli_octavia.price)
print('year of issue:' ,Zhyguli_octavia.year_of_issue)
Zhyguli_octavia.car_price(2000)
print('price is: ', Zhyguli_octavia.price)

Zhyguli_octavia.new_color('Gold')
print('color is: ', Zhyguli_octavia.color)

print(Zhyguli_octavia._model)
Zhyguli_octavia.new_model()
print(Zhyguli_octavia._model)

Zhyguli_octavia.year_of_issue = 2000
Zhyguli_octavia.year_OF_issue()

print('Our car is Zhyguli Octavia',
      '\nmodel is:', Zhyguli_octavia._model ,
      '\nprice is: ',Zhyguli_octavia.price,
      '\ncolor is: ',Zhyguli_octavia.color,
      '\nyear of issue:',Zhyguli_octavia.year_of_issue,
      '\nengine capacity is:',Zhyguli_octavia.engine_capacity)


'''
Задание 2

Реализуйте класс «Книга». 
Необходимо хранить в полях класса: 
название книги, 
год выпуска, 
издателя, 
жанр, 
автора, 
цену. 
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''

class Book:
    name = ''
    date_of_issue = 2022
    _publisher = 'Knizhniy_klub'
    style = ''
    author = "Bandera_Stepan"
    price = 100


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


The_Da_Vinci_Code = Book()

The_Da_Vinci_Code.name = 'The_Da_Vinci_Code'
print('The book name is:', The_Da_Vinci_Code.name)

print(The_Da_Vinci_Code.date_of_issue)

The_Da_Vinci_Code.book_style()

The_Da_Vinci_Code.book_style("Horror")

The_Da_Vinci_Code.book_price()
print(The_Da_Vinci_Code.book_price())

The_Da_Vinci_Code.book_style("Fantasy")

print(The_Da_Vinci_Code.style)
The_Da_Vinci_Code.book_price()
print(The_Da_Vinci_Code.book_price())
print(The_Da_Vinci_Code.date_of_issue,","
      ,'the price is:', The_Da_Vinci_Code.book_price(),
      ",", The_Da_Vinci_Code.name,
      ",","Author:", The_Da_Vinci_Code.author)



''''
Задание 3

Реализуйте класс «Стадион». 
Необходимо хранить в полях класса: 
- название стадиона, 
- дату открытия, 
- страну, 
- город, 
- вместимость. 
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''
class Stadium:
    name = ''
    opening_date = '24.02.2022'
    country = " "
    city = " "
    capacity = 1000

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

Dinamo = Stadium()

Dinamo.stadium_name('Dinamo')
print(Dinamo.name)

print("opening date is:", Dinamo.opening_date)

Dinamo.stadium_country("Ukraine")
print(Dinamo.country)

Dinamo.stadium_city("Odessa")
print(Dinamo.city)

Dinamo.add_PEOPLE()
print(Dinamo.capacity)
Dinamo.add_PEOPLE()
print(Dinamo.capacity)
Dinamo.add_PEOPLE()
print(Dinamo.capacity)

Azov = Stadium()
Azov.stadium_name("Azov")
print(Azov.name)

print("opening date is:", Azov.opening_date)

Azov.add_PEOPLE()
print(Azov.capacity)
Azov.add_PEOPLE()
print(Azov.capacity)

Azov.change_date("01.04.2022")
print("opening date is:", Azov.opening_date)
















