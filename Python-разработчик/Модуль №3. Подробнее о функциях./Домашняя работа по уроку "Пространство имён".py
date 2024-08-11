calls = 0

def count_calls():
    print(calls)

def string_info_manual(): # Function for string evaluation with manual input
    global calls
    calls = calls + 1
    list = input('Введите тестовую строку: ')
    tmp1, tmp2 = list.upper(), list.lower()
    result = (len(list), tmp1, tmp2)
    print(result)

def string_info(list): # Function with data input over arguments
    global calls
    calls = calls + 1
    tmp1, tmp2 = list.upper(), list.lower()
    result = (len(list), tmp1, tmp2)
    print(result)

def repitable_string_info(): # Repitable function for string evaluation
    string_info()
    again = str(input('Проанализировать еще одну строку? (да/нет) '))
    while again == 'да':
        string_info()
        again = str(input('Проанализировать еще одну строку? (да/нет) '))
    print('Функция завершена')

def is_contains(string, list_to_search):
    global calls
    calls = calls + 1
    for i in range(len(list_to_search)):
        tmp = list_to_search[i].upper()
        res = tmp.__contains__(string.upper())
        if res == True:
            print(res)
            break
        elif res == False:
            print(res)
            break




string_info('Capybara')
string_info("Armageddon")
is_contains('Urban', ['UrbaN', 'banana', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
count_calls()




