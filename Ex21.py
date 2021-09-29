def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"ADDING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def power(a, b):
    print(f"{a} to the power of {b}")
    return a ** b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(76, 7)
weight = multiply(5, 32)
iq = divide(42, 6)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a Puzzle!")

what = add(age, substract(height,multiply(weight,divide(iq,2))))

print("That Becomes: ", what, " can you do it by hand?")

result = power(2,3)
print(f"Result: {result}")
