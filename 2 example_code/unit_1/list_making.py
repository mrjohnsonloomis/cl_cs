# Start with a basic shopping list

shopping = ['milk', 'bread', 'eggs']
print(f'Initial Shopping List: {shopping}')

# Adding an item to a list
shopping.append('cheese')
print(f'After adding cheese: {shopping}')

# Add to a specific index
shopping.insert(0, 'coffee')
print(f'After adding coffee: {shopping}')

# Remove a given value
print('Remove items with remove()')
shopping.remove('bread')
print(f'After removing bread: {shopping}')

# Using pop() to check off item at the end of the list
last_item = shopping.pop()
print(f'got {last_item}!')
print(f'Remaining list is: {shopping}')

# Sort the list
shopping.sort()
print(shopping)

# Reverse the list
shopping.reverse()
print(shopping)