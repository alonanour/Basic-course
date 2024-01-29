import string

my_digits = str(string.digits)
my_digits = my_digits + "."

is_true = True
while is_true:
    number_1 = input("Введіть перше число: ")
    number_2 = input("Введіть друге число: ")
    if all(num in my_digits for num in number_1) and all(num in my_digits for num in number_2) is True:
        act = input("Напишіть яку дію над цими числами ви хочете зробити: ")
    else:
        continue
    result = None
    if act == "+":
        result = float(number_1) + float(number_2)
    elif act == "-":
        result = float(number_1) - float(number_2)
    elif act == "*":
        result = float(number_1) * float(number_2)
    elif act == "/":
        if number_2 == "0":
            result = "Дільник не може дорівнювати нулю"
        else:
            result = float(number_1) / float(number_2)
    else:
        result = ("Ви зробили щось не так")
    print(result)
    while True:
        answer = input("Ви хочете продовжити?: ")
        if answer == "так":
            break
        elif answer == "ні":
            is_true = False
            break