# ООП
# a = int(5)
# b = str('Hello')
# c = list([1, 2, 3])

# class Box:
#     v = 5
#     def open(self):
#         print('Open box')
#
# lanch = Box()
# print(lanch.v)
# lanch.open(2)
#
#
# tools = Box()
# tools.open(5)

class Borsch:
    volume = 3
    color = 'red'
    components = ['Beetroots','tomatoes', 'Cabbage', 'Potatoes', 'Been', 'Meat','Salt', 'Bay_Leaf']
    temperature = 20.5
    vegetarian = False
    create_date = '22/02/2022'
    life_period = 480

    def heating(self):
        self.temperature = self.temperature + 5
    def show_heating(self):
        return self.temperature

    def more_borsch(self):
        self.volume = self.volume + 3
    def show_volume(self):
        return self.volume

    def change_color(self,new_color):
        self.color = new_color
    def show_color(self):
        return self.color


olgas_borsch = Borsch()
print(olgas_borsch.show_heating())
olgas_borsch.heating()
olgas_borsch.heating()
olgas_borsch.more_borsch()
print(olgas_borsch.show_heating(),'\nHow much of Borsch do you want?: ', olgas_borsch.show_volume())
andrii_borsch = Borsch()
print(andrii_borsch.show_volume())
andrii_borsch.more_borsch()
print(andrii_borsch.show_volume())
andrii_borsch.color = 'Green'
print(andrii_borsch.show_color())






