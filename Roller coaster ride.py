print("Welcome to roller coaster ride!")
height= int(input("Your Height in cm: "))
age= int(input("Your age please: "))
bill = 0
if height >= 160:
    print("You are good to go!!!")
    if age < 12:
        bill = 5
        print("Childern price is 5$")
    elif age <= 18:
        bill = 10
        print("Youth price is 10$")
    elif  age >= 45  or age <= 55:
        print("Your Ticket is free! Enjoy")
    else:
        bill = 15
        print("Adult price is 15$")
    picture= input("Do you want a photo for your ride: Y or N: ")
    if picture == "Y":
     bill +=3

    print(f"Your final bill is {bill}$")
else:
    print("Grow up buddy!")    

