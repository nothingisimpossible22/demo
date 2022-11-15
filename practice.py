
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

print("coding is fun")

print("This is created after featurex and test branch create")

def simple():
    return "simple"

print("After branch featurex2 created")
def featurex2_branch():
    return "featurex2 branch created"

def greet():
    return "Hello World"

def which_branch():
    return "This is featurex3"