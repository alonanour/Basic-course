number_1 = input("Введіть перше число: ")
number_2 = input("Введіть друге число: ")
act = input("Напишіть яку дію над цими числами ви хочете зробити: ")

if act == "додавання" or act == "додати" or act == "+":
    print(float(number_1) + float(number_2))
elif act == "віднімання" or act == "відняти" or act == "-":
    print(float(number_1) - float(number_2))
elif act == "множення" or act == "помножити" or act == "*":
    print(float(number_1) * float(number_2))
elif act == "ділення" or act == "поділити" or act == ":" or act == "/":
    if number_2 == "0":
        print("Дільник не може дорівнювати нулю")
    else:
        print(float(number_1) / float(number_2))
else:
    print("Ви зробили щось не так")