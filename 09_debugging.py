text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)

print("give me a number")
n = input()

for num in range(1, 20):
    if num % 2 <= 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

num = int(input("Enter an integer: "))
if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num + 1):
    result *= i   

  print("Factorial of " + str(num) + " is " + str(result))

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts > 3:
        print("Too many attempts")
        break
    attempts += 1