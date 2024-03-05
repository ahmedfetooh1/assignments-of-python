# # Input
# "     osAmA   "

# Needed Output

# "Hello Osama, Happy To See You Here."

name = input ('please enter your name :').strip().capitalize()
print(f"hello {name}, Happy To see you here.")

print("="*50)

# Inputs

16 # Input One
24 # Input Two

# Needed Output

 # If Age < 16
 # If Age Is 16+

age = int(input("enter you age : "))
if age <16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is{age}, All Articles Is Suitable For You")

print('='*50)

# Inputs

# "Osama" # First Name
# "Mohamed" # Second Name

# Needed Output

# ." # Example "Osama M."

firstname = input('please enter the first anme : ').strip().capitalize()
secondname = input ("enter you second name : ").strip().capitalize()
print (f"Hello {firstname} {secondname:.1s} ")

print("="*50)

email = input("enter you email : ").strip().lower()
username = email[:email.index('@')].capitalize()
print(f"your name is {username}")
provider = email[email.index("@") + 1 :email.index(".")]
print(f"Email Service Provider Is {provider}")
domain = email[email.index('.') +1:]
print(f"top level domain is {domain}")

print("="*50)
