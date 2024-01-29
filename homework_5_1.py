import keyword
import string

name = input("Напишіть ім'я змінної: ")

my_punctuation = str(string.punctuation)
my_punctuation = my_punctuation.replace("_", "")

if name == "_":
    result = True
elif any(char in my_punctuation for char in name) is True:
    result = False
elif name.isdigit() is True:
    result = False
elif name[0].isdigit() is True:
    result = False
elif keyword.iskeyword(name) is True:
    result = False
elif name.islower() is False:
    result = False
elif name.find(" ") != -1:
    result = False
else:
    result = True
print(result)