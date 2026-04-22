x = 10
y = 5
x += 3
y -= 2
result = x / y 
print(f"The result of the operation is {result}")

a = 15
b = 10
c = 8 
condition1 = a > b 
condition2 = b % c == 0
condition3 = c <= a
final_condition = condition1 (condition2 and condition3)
print(f"The final condition is {final_condition}")

score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:   
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:    print("Grade: F")
print(f"Your grade is: {score}")
