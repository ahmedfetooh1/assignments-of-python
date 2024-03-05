#"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name = "osama"
age = "38"
country = "Egypt"

print(f"\"hello \'{name}\',How you doing \\ \"\"\" your age is \"{age}\"\" + and your country is : {country}")

print("="*50)

# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

print(f""" " hello '{name}' , how you doing \ 
\"""your age is "{age}"" + 
and your country is : {country}   """)

print("="*50)



# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"

name = 'Elzero'
print(f"second letter is \"{name[1]}\"")
print(f"third letter is \"{name[2]}\"")
print(f"last letter is \"{name[-1]}\"")

print("="*50)

name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"

print(name[1:4])
print(name[::2])
print(f"{name[4]}{name[2]}{name[0]}")

print("="*50)

name = "#@#@Elzero#@#@"

# Needed Output
# Elzero
print(name.strip("#@"))

print("="*50)

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

print("="*50)

name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

print("="*50)

name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma
print(name_one.swapcase())
print(name_two.swapcase())

print("="*50)

msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# 2
print(msg.count("Love"))

print("="*50)

name = "Elzero"

# Needed Output
# 2
print(name.index("z"))

print("="*50)

msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School

print(msg.replace("3","Love",1))

print("="*50)

msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although Love Elzero Web School
print(msg.replace("3","Love"))

print("="*50)

name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print(f"My name is {name},and my age is {age:,d} , and my country is {country}")

print("="*50)

