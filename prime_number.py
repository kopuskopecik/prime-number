# finding prime number
a = input("Please enter a positive integer: ")
while not a.isdigit() or int(a) == 1 or int(a) == 0:
    a = input("Please enter a positive an integer exclude 1 and 0")
a = int(a)
counter = 0
if a == 2:
    print(a, "is a prime number")
else:
    for i in range(2, a):
        if a % i == 0:
            print(a, "is a not prime number")
            counter+= 1
            break
    if not counter:
        print(a, "is a prime number")