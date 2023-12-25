fruits = ['apple', 'banana', 'orange']

fruits.append('kiwi')
print(fruits)

fruits.insert(1, 'grape')
print(fruits)

more_fruits = ['pineapple', 'mango']
fruits.extend(more_fruits)
print(fruits)



fruits.remove('banana')
print(fruits)

del fruits[1]
print(fruits)

last_fruit = fruits.pop()
print(last_fruit)
print(fruits)



colors = ('red', 'green', 'blue')
more_colors = ('yellow', 'purple')

all_colors = colors + more_colors
print(all_colors)
