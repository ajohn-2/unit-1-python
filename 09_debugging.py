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

