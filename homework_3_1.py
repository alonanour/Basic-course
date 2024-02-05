# Завдання 1 Найпростіший калькулятор
#
# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії,
# обчислює та друкує результат.
#
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

number_1 = input("Введіть перше число: ")
number_2 = input("Введіть друге число: ")
act = input("Напишіть яку дію над цими числами ви хочете зробити: ")

if act == "додавання" or act == "додати" or act == "+":
    result = float(number_1) + float(number_2)
elif act == "віднімання" or act == "відняти" or act == "-":
    result = float(number_1) - float(number_2)
elif act == "множення" or act == "помножити" or act == "*":
    result = float(number_1) * float(number_2)
elif act == "ділення" or act == "поділити" or act == ":" or act == "/":
    if number_2 == "0":
        result = "Дільник не може дорівнювати нулю"
    else:
        result = float(number_1) / float(number_2)
else:
    result = "Ви зробили щось не так"

print(result)