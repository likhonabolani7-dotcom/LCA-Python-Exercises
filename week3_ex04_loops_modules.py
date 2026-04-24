fruits = ["apple", "banana", "cherry", "mango", "grape  "]
for fruit in fruits:
    print(fruits)

count = 10
while count >= 0:
    print(count)
    count -= 1  

    for i in range(1,11):
        print(i)

import random
colors = ["red", "green", "blue", "yellow", "purple"]

for _ in range(5):
    random_color = random.choice(colors)
    print(random_color) 
    
import math_operations
def main():
    num1 = 10
    num2 = 5
    sum_result = math_operations.add(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")
    
    difference_result = math_operations.subtract(num1, num2)
    print(f"The difference between {num1} and {num2} is {difference_result}")
    
    product_result = math_operations.multiply(num1, num2)
    print(f"The product of {num1} and {num2} is {product_result}")
    
    quotient_result = math_operations.divide(num1, num2)
    print(f"The quotient of {num1} divided by {num2} is {quotient_result}")

if __name__ == "__main__":
    main()  