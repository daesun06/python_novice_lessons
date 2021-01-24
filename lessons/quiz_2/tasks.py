# Задание 1. Создайте программу для
# Определения четности или не четности числа
# Функция должна принимать int на вход
# На выходе она должна возвращать True если число четное и
# False если число не четное
# Программа должна запускаться без ошибок!
# За правильное выполнение выдается 6 баллов!
 
def even_or_odd(number:int):
    if number % 2 == 0:
        return True
    else:
        return False

print(even_or_odd(7)) # 5 points 


# Задание 2. Создайте программу которая выполняет следующее
#  Функция должна принимать str на вход
# Если значение на входе равно 'male' то напечатайте "Hello I am a boy"
# Если значение на входе равно 'female' то напечатайте "Hello I am a girl"
# Иначе для всех остальных значений функция должна напечатать "Incorrect value given!"
# Программа должна запускаться без ошибок!
# За правильное выполнение выдается 6 баллов!
 
def male_or_female(name):
    if name == "male":
        print("Hello i am a boy!")
    elif name == "female":
        print("Hello i am a girl!")
    else:
        print("Incorrect value given!")

male_or_female("deson") # 6 points 

# Задание 3. Создайте класс Clock которая содержит функцию get_time.
# Функция get_time должна использовать функцию asctime из модуля time и печатать текущее время в терминал.
# За правильное выполнение выдается 6 баллов!
# Бонус балл - добавьте конструктор в класс который будет принимать переменную name.
# Вместо времени функция get_time должна печатать 'Hello {name} here is current time {time}'.
# Где переменные name и time представляют значение name переданное в конструктор и time из
# функции asctime из модуля time.

import time
class Clock: # ошибка
    def get_time(self):
        print(time.asctime()) 
# Hint 1 - minus 1 point

clock = Clock()
print(clock.get_time())
# 14 out of 18 