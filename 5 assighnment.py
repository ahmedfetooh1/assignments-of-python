# Needed Output

# "Osama"
# <class 'tuple'>

mytuple = "Osama",
print(mytuple)
print(type(mytuple))

print("="*50)

friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements

# friends[0]='Elzero'
print(friends)
print(type(friends))
print(len(friends))

print("="*50)

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
newnums=nums + letters
print(f"nums_and letters_one_ = {newnums}")
print(len(newnums))

print("="*50)

my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4

a,b,_,c = my_tuple
print(a)
print(b)
print(c)

print("="*50)

