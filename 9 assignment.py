# Inputs

# num1 = 20
# num2 = 40
# operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

num1 = int(input('enter the first num :'))
num2 = int(input('enter the second num : '))
operator = input('enter the operator : ').strip()
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2 )
elif operator == "/":
    print(num1 / num2)
else:
    print("there is wrong in inputs")

print("="*50)

age = 16
print("App is sutible for you " if age > 14 else "App  is not sutible for you")

print('='*50)

aged = int(input("enter your age "))
if aged in range(1,100):
    print(f"your age in years is {aged}")
    month = aged *12
    print(f"your age in mounth is {month}")
    weeks = month * 4
    print(f"your age in weeks is {weeks}")
    days = weeks *7 
    print(f"your age in days is {days}")
    hours =days *24
    print(f"your age in hours is {hours:,d}")
    minutes = hours *60
    print(f"your age in minutes is {minutes:,d}")
else:
    print("age unknwon")

print("="*50)

# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

# Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

if country in countries :
    print(f"your country eligible for discount and the price after discount is {price - discount}$")
else:
    print(f'your country not eligible for discount and the price is {price}$')

print("="*50)

