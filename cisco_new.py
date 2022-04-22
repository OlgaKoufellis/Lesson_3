zero = '###\n# #\n# #\n# #\n###'.split('\n')
one = '  #\n  #\n  #\n  #\n  #'.split('\n')
two = '###\n  #\n###\n#  \n###'.split('\n')
three = '###\n  #\n###\n  #\n###'.split('\n')
four = '# #\n# #\n###\n  #\n  #'.split('\n')
five = '###\n#  \n###\n  #\n###'.split('\n')
six = '###\n#  \n###\n# #\n###'.split('\n')
seven = '###\n  #\n  #\n  #\n  #'.split('\n')
eight = '###\n# #\n###\n# #\n###'.split('\n')
nine = '###\n# #\n###\n  #\n###'.split('\n')
# print(zero)#Посмотрите сюда, я делаю каждую строку отдельным элементом
def digit(num):
    while True:
        try:
            str_num = str(num)
            list_num = list(str_num)
            digit_result = ''
            for i in range(5):#так как в цифре 5 строк ['###', '# #', '# #', '# #', '###']
                for number in range(len(list_num)):
                    if list_num[number] == '0':
                        digit_result += zero[i]
                    if list_num[number] == '1':
                        digit_result += one[i]
                    if list_num[number] == '2':
                        digit_result += two[i]
                    if list_num[number] == '3':
                        digit_result += three[i]
                    if list_num[number] == '4':
                        digit_result += four[i]
                    if list_num[number] == '5':
                        digit_result += five[i]
                    if list_num[number] == '6':
                        digit_result += six[i]
                    if list_num[number] == '7':
                        digit_result += seven[i]
                    if list_num[number] == '8':
                        digit_result += eight[i]
                    if list_num[number] == '9':
                        digit_result += nine[i]
                    digit_result = digit_result + '  '
                digit_result = digit_result + '\n'
        except ValueError:
            continue
        return digit_result

num = int(input('Please, enter non-negative integer number:'))
print(digit(num))