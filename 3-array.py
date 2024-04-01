expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?

# O(1)
print(expenses[1] - expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.

# O(1)
print(sum(expenses[0:2]))

# 3. Find out if you spent exactly 2000 dollars in any month

# O(n)
any_exact = False
for expense in expenses:
    if expense == 2000:
        any_exact = True
        break

print(any_exact)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

# O(1)
expenses.append(1980)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# O(1)
expenses[3] -= 200


# PROBLEM 2
# You have a list of your favourite marvel super heros.


heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

# 1. Length of the list

# O(1)
print(len(heros))

# 2. Add 'black panther' at the end of this list

# O(1)
heros.append("black panther")

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
hulk_index = heros.index("hulk")
heros.insert(hulk_index + 1, "black panther")

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros[1:3] = ["doctor strange"]

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)
