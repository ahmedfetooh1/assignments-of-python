my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

ununique = set(my_list)
mylist = list(ununique)
print(mylist)
print(type(mylist))
mylist.remove(5)
print(mylist)

print("="*50)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
c = nums.union(letters)
print(c)
c= nums | letters 
print(c)
nums.update(letters)
print(nums)

print("="*50)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
my_set.discard("C")
print(my_set)

print("="*50)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
#True
print(set_one.issubset(set_two))

print("="*50)

# Create Dictionary Here

# Needed Output

"HTML Progress Is 90%"
"CSS Progress Is 80%"
"Python Progress Is 30%"
"AI Progress Is 20%"

mydict = {
    "HTML":"90%",
    "CSS":"80%",
    "Python":"30",
    "AI":"20%"
}
mydict["ML"]="10%"
print(mydict)


print("="*50)