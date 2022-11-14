
def fizz_buzz(n):
    for i in range(n):
        if i % 3 == 0 and n % 5 == 0:
            print("fizz_buzz")
        elif i % 3 == 0:
            print("buzz")
        elif i % 5 == 0:
            print("fiz")
        else:
            print(i)
                        
print(fizz_buzz(6))

print("This is for test")

print("What will happen after this")