from code import interact


_author__ = 'Хайруллин Руслан Ривкатович'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

name = int(input("сколько вам лет: "))
if name >= 18:
    print("доступ разрешен")
else:
    print('Извините, пользоваться данным ресурсом можно только с 18 лет')
    

# Зу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for inадача-2: Напишите программ
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

name = (input('четные или нечетные?'))
r = 'четные'
n = 'нечетные'
t = 'я не понимаю'
if name == (n):
    for i in range (1,20+1):
        if i % 2 == 0:
            continue
        print (i)
elif name == (r):
    for x in range (1,20+1):
        if x % 2 == 1:
            continue
        print (x)
elif t != r != n:  
    print (t)     
  
     
        
    



   





# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
x = input('Введите число: ')
print(max(x))