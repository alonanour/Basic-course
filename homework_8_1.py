# Завдання 1
#
# Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом.
# До нього необхідно додати 1.
#
# Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму,
# знову розбити на список із цифр.
#
# В результаті функція повертає список із цифр, що становлять значення суми.
#
# Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235.
# Після цього потрібно розбити отримане число на складові цифри.
# У результаті має бути список [1, 2, 3, 5], який повертає функція.
#
# Test:
#
# def add_one(some_list):
#     pass
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

def add_one(some_list):
    length_number = len(some_list)
    number = ""
    for num in range(length_number):
        number = number + str(some_list[num])
    number = str(int(number) + 1)
    my_list = []
    for i in number:
        my_list.append(int(i))
    return my_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")