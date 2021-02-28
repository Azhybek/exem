# # 1 list

lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
dic = {}
for index,value in enumerate(lst):
    dic[index]=value
print(dic)

# # 2 игра "угадай число"

import random
guesses = 0
guesses_finale = int(input("Число попыток: "))
print("Игра Угадай число")
a = int(input("Рандом число от: "))
b = int(input("Рандом число от: "))
print("Угадайте число от:", a, "-", b, "у вас", guesses_finale, "попыток")
random_number = random.randint(a, b)
while guesses < guesses_finale:
    number = int(input("Загадайте число: "))
    guesses += 1
    if random_number > number:
        print("слишком мало")
    elif random_number < number:
        print("слишком много")
    else:
        break
if number == random_number:
    print("Класс! Вы угадали")
else:
    print("Все, вы не выиграли. Игра завершилась")

# # 3 string

some_word = input("Введите имя нечетной длины больше 7 символов: ")
number_word = int((len(some_word) // 2) + (1))
print(some_word[number_word-2]+some_word[number_word-1]+some_word[number_word])

# # 4

print("Введите 2 имя с одинаковой длиной")
name_boys = input("Введите имя парня: ")
name_girls = input("Введите имя девушки: ")
len_name = int((len(name_boys) + len(name_girls)) / (2))
name= ""
for i in range(len_name):
    name += name_boys[i] + name_girls[i]
print(name)

