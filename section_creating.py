name = input("Enter your name")
age = int(input("Enter your age"))
height = float(input("Enter your height"))
user_profile = [name, age, height , True]
print(f"User {name} is {age} years old and his/her height is {height}")
section = int(input("Enter your section"))
print({user_profile[section]})
