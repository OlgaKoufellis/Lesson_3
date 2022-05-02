# def average(*numbers):
#     # *numbers - это кортеж
#     count = len(numbers)
#     sum = 0
#     for number in numbers:
#         sum = sum + number
#     return sum/count
# print(average(1,2,3,4,5,6,7,8,9,0,2,4,5))
# print(average(1,3))


import math
import turtle
def xt(t):
    return 16 * math.sin(t) **3
def yt(t):
    return 13 * math.cos(t) - 5 * \
            math.cos(2 * t) - 2 * \
            math.cos(3 * t) - \
            math.cos(4 * t)
t = turtle.Turtle()
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255-i) % 255, i % 255, (255+i)//2%255)
    t.goto(0, 0)
t.hideturtle()
turtle.update()
turtle.mainloop()




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(6))


