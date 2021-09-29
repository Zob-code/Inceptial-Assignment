from sys import argv

print("How old are you ?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you  weight?",end=" ")
weight = input()

print(f"So, You're {age} old, {height} tall and {weight} heavy.")


script, filename = argv

txt = open(filename)

print(f"Here' your file {filename}:")
print(txt.read)

print("Type the file name again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print("Let's practice everything")
print("You\'d need to know \'bout escapes with \\ that do:")


poem = """
\t The lovely world
with logic so firmly planted
cannot dicern \n the needs of love
nor comprehensed pasion form instution
and requires an explanation
\n\t\t wheere there is none.
"""

print("---------")
print(poem)
print("---------")

five = 10 - 2 + 3 - 6

print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, {} crates".format(*formula))



people = 20
cats = 30
dogs = 15

if people < cats :
    print("Too many cats the world is doomed!")

if people > cats:
    print("not so many cats the world is safe")

if people < dogs:
    print("The world is drooled on1")

if people > dogs:
    print("The world is dry")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs")
if people <= dogs:
    print("People are lesser than or equal to the dogs")
if people == dogs:
    print("people are dogs")
