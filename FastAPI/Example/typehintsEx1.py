def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


res1 = get_full_name("John", " Doe")
print(res1)
res2 = get_name_with_age("John", "30")
print(res2)