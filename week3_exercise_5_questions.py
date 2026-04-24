fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)
fruits.insert(0, "grape")
print(fruits)
fruits.remove("banana")
print(fruits)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
total_sum = sum(numbers)
print(f"The sum of the numbers is {total_sum}")
average = total_sum / len(numbers)
print(f"The average of the numbers is {average}")

capitals = {"USA": "Washington, D.C.", "France": "Paris", "Japan": "Tokyo"}
print(capitals["France"])
capitals["Germany"] = "Berlin"
print(capitals)
del capitals["USA"]
print(capitals)

fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(f"fruits:{list(fruit_colors.keys())}")
for fruit, color in fruit_colors.items():
    print(f"{fruit} is {color}")
target_fruit = "banana"
if target_fruit in fruit_colors:
    print(f"{target_fruit} is {fruit_colors[target_fruit]}")
    


