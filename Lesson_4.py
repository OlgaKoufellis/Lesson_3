age = 18 # PEP 8 CISCO
if age < 18: #True
    print('Child')
if age >= 18:
    print('Adult')

age = 18 # PEP 8 CISCO
if age <= 18: #True
    print('Child')
if age >= 18:
    print('Adult')

age = 18
if age <= 18:
    print('Child')
else:
    print('Adult')

age = 13 # PEP 8 CISCO
if age <= 18: #True
    print('Child')
else:
    print('Adult')


weight = 120
#если вес мень 150 выводит вес если вес больше 150 выводит привышено значение

weight = 120
if weight <= 150:
    print(weight)
else:
    print('Attention!!!!')


age = -20
if age < 0:
    print('ERROR')  #else if
elif age <= 18:
    print('Child')
else:
    print('Adult')



age = 13
if age < 0:
    print('ERROR')  #else if
elif age < 18:
    print('Child')
elif age < 13:
    print('Teen')
else:
    print('Adult')
print('TRIS')




age = 1100
if age < 0:
    print('ERROR')  #else if
elif age < 13:
    print('Child')
elif age < 18:
    print('Teen')
elif age < 135:
    print('Adult')
else:
    print('you are dead')


weight = 25
if weight <0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <=60:
    print('your weight is perfect!!!')
elif weight <=150:
    print('OMG!!!')



weight = 120
if type(weight) != type(1):
    print('yNo txt allowed')
if weight <0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <=60:
    print('your weight is perfect!!!')
elif weight <=150:
    print('OMG!!!')


weight = 120
if type(weight) == type(1):
    print('Text type')
elif type(weight) ==type(1.0):
    print("Float type")
if weight <0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <=60:
    print('your weight is perfect!!!')
elif weight <=150:
    print('OMG!!!')
