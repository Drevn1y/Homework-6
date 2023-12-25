fruits = ['apple', 'banana', 'orange']
print(fruits[0])
fruits[1] = 'grape'
print(fruits)
fruits.append('kiwi')
print(fruits)
fruits.remove('grape')
print(fruits)
print(len(fruits))

colors = ('red', 'green', 'blue')
print(colors[0])
new_colors = colors + ('yellow', 'purple')
print(new_colors)
first_color, second_color, third_color = colors
print(first_color)
print(len(colors))
