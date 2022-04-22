zero = '###\n# #\n# #\n# #\n###'
one = '  #\n  #\n  #\n  #\n  #'
two = '###\n  #\n###\n# \n###'
three = '###\n #\n #\n###\n #\n###'
four = '# #\n# #\n###\n  #\n  #'
five = '###\n#  \n###\n  #\n###'
six = '###\n# \n###\n# #\n###'
seven = '###\n  #\n  #\n  #\n  #'
eight = '###\n# #\n###\n# #\n###'
nine = '###\n# #\n###\n  #\n###'

def digit(num):
    while True:
        try:
            str_num = str(num)
            list_num = list(str_num)
            digit_result = ''
            for number in range(len(list_num)):
                if list_num[number] == '0':
                    digit_result += zero
                if list_num[number] == '1':
                    digit_result += one
                if list_num[number] == '2':
                    digit_result += two
                if list_num[number] == '3':
                    digit_result += three
                if list_num[number] == '4':
                    digit_result += four
                if list_num[number] == '5':
                    digit_result += five
                if list_num[number] == '6':
                    digit_result += six
                if list_num[number] == '7':
                    digit_result += seven
                if list_num[number] == '8':
                    digit_result += eight
                if list_num[number] == '9':
                    digit_result += nine
        except ValueError:
            continue
        # return digit_result

num = int(input('Please, enter non-negative integer number:'))
print(digit(num))