import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_items = len(names)

random_choice = random.randint(0, total_items - 1)

person_pay = names[random_choice]

print(f"{person_pay} is going to buy the meal today!")
