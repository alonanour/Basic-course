num = input("Введіть 4-х значне число: ")

result_1 = int(num) // 1000
result_2 = int(num) // 100 % 10
result_3 = int(num) // 10 % 10
result_4 = int(num) % 10
print(result_1)
print(result_2)
print(result_3)
print(result_4)