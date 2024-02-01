list_of_people = [
    {"name": "Ann", "age": 23},
    {"name": "Emma", "age": 31},
    {"name": "Sofiia", "age": 18},
    {"name": "Alice", "age": 20},
    {"name": "Mariia", "age": 18},
    {"name": "Yana", "age": 33},
    {"name": "Marina", "age": 27},
]

youngest_age = 200
longest_name = []
total_age = 0
total_people = len(list_of_people)

for person in list_of_people:
    if person["age"] < youngest_age:
        youngest_age = person["age"]
        list_of_youngest_people = [person["name"]]
    elif person["age"] == youngest_age:
        list_of_youngest_people.append(person["name"])

    if len(person["name"]) > len(longest_name):
        longest_name = person["name"]
        list_of_longest_names = [person["name"]]
    elif len(person["name"]) == len(longest_name):
        list_of_longest_names.append(person["name"])

    total_age += person["age"]
average_age = total_age / total_people

print(f"A list of the youngest people: {list_of_youngest_people}"
      f"\nA list of the longest names: {list_of_longest_names}"
      f"\nAverage age of people from the list: {average_age}")