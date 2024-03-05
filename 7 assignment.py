print(bool(True))
print(bool(10))
print(bool("ahmd"))
print(bool([1,2]))

print(bool(False))
print(bool([]))
print(bool(0))
print(bool(""))

print("="*50)

html = 80
css = 60
javascript = 70

# Needed Output
#True
print(bool(html > 50))
print(bool(css > 50))
print(bool(javascript> 50))

print("="*50)

num_one = 10
num_two = 20
num = 20

# Needed Output

# True
# False

print(bool(num > (num_one or num_two)))
print(bool(num >( num_one and num_two)))

print("="*50)

num_one = 10
num_two = 20

# Needed Output

# 30
# 27000
# 1000
# 200.0
# <class 'str'>
result =int( num_one + num_two)
print(result)
result2 =result ** 3
print(result2)
result3 = result2 % 26000
print(result3)
result4 =float(result3 / 5)
print(result4)
result5 = str(result4)
print(type(result5))

print("="*50)
