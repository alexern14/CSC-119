#PYTHON TUPLE EXAMPLES

#
# 1. Python program that creates tuples
#

# Zero-element tuple.
a = ()
# One-element tuple.
b = ("one",)
# Two-element tuple.
c = ("one", "two")

print(a)
print(len(a))

print(b)
print(len(b))

print(c)
print(len(c))

#
# 2. Python program that assigns tuple
#

tuple = ('cat', 'dog', 'mouse')

# This causes an error.
tuple[0] = 'feline'

#Results

# TypeError: 'tuple' object does not support item assignment

#
# 3.Python program that uses tuples, no parentheses
#

# A trailing comma indicates a tuple.
one_item = "cat",

# A tuple can be specified with no parentheses.
two_items = "cat", "dog"

print(one_item)
print(two_items)

#
# 4.Python program that adds and multiples tuples
#

checks = (10, 20, 30)

# Add two tuples.
more = checks + checks
print(more)

# Multiply tuple.
total = checks * 3
print(total)

#
# 5. Python that searches tuples
#

pair = ("dog", "cat")

# Search for a value.
if "cat" in pair:
    print("Cat found")

# Search for a value not present.
if "bird" not in pair:
    print("Bird not found")

    
#PYTHON LIST EXAMPLES

#
# 1. Python program that uses append
#

list = []
list.append(1)
list.append(2)
list.append(6)
list.append(3)

print(list)

#
#  2. Python program that calls insert
#

list = ["dot", "perls"]

# Insert at index 1.
list.insert(1, "net")

print(list)

Output

#
# 3. Python program that uses in
#

items = ["book", "computer", "keys", "mug"]

if "computer" in items:
    print(1)

if "atlas" in items:
    # This is not reached.
    print(2)
else:
    print(3)

if "marker" not in items:
    print(4)

['dot', 'net', 'perls']


#
# 4. Python program that sorts and reverses
#

list = [400, 500, 100, 2000]

# Reversed.
list.reverse()
print(list)

# Sorted.
list.sort()
print(list)

# Sorted and reversed.
list.reverse()
print(list)

#
# 5. Python that removes elements
#

names = ["Tommy", "Bill", "Janet", "Bill", "Stacy"]

# Remove this value.
names.remove("Bill")
print(names)

# Delete all except first two elements.
del names[2:]
print(names)

# Delete all except last element.
del names[:1]
print(names)

#
# 6. Python that uses for, list
#

# An input list.
elements = ["spider", "moth", "butterfly", "lizard"]

# Use simple for-loop.
for element in elements:
    print(element)

#
#PYTHON DICTIONARY EXAMPLES

#
#  1.  Python program that gets values
#

plants = {}

# Add three key-value tuples to the dictionary.
plants["radish"] = 2
plants["squash"] = 4
plants["carrot"] = 7

# Get syntax 1.
print(plants["radish"])

# Get syntax 2.
print(plants.get("tuna"))
print(plants.get("tuna", "no tuna found"))

#
# 2. Python program that causes KeyError

lookup = {"cat": 1, "dog": 2}

# The dictionary has no fish key!
print(lookup["fish"])

#Output

#Traceback (most recent call last):
#  File "C:\programs\file.py", line 5, in <module>
#    print(lookup["fish"])
# KeyError: 'fish'

#
# 3. Python program that uses in
#

animals = {}
animals["monkey"] = 1
animals["tuna"] = 2
animals["giraffe"] = 4

# Use in.
if "tuna" in animals:
    print("Has tuna")
else:
    print("No tuna")

# Use in on nonexistent key.
if "elephant" in animals:
    print("Has elephant")
else:
    print("No elephant")
    
#
# 4. Python program that uses keys
#

hits = {"home": 125, "sitemap": 27, "about": 43}
keys = hits.keys()
values = hits.values()

print("Keys:")
print(keys)
print(len(keys))

print("Values:")
print(values)
print(len(values))

#
# 5. Python that loops over dictionary
#

plants = {"radish": 2, "squash": 4, "carrot": 7}

# Loop over dictionary directly.
# ... This only accesses keys.
for plant in plants:
    print(plant)

#
# 6. Python that counts letter frequencies
#

# The first three letters are repeated.
letters = "abcabcdefghi"

frequencies = {}
for c in letters:
    # If no key exists, get returns the value 0.
    # ... We then add one to increase the frequency.
    # ... So we start at 1 and progress to 2 and then 3.
    frequencies[c] = frequencies.get(c, 0) + 1

for f in frequencies.items():
    # Print the tuple pair.
    print(f)
    
