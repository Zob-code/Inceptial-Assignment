people = 20
cars = 30
trucks = 15

if cars > people:
    print("We should take the car")

elif cars < people:
    print("We should not take the car.")

else:
    print("We can't decide")

if trucks > cars:
    print("That's too much trucks")

elif trucks < cars:
    print("May be we should take the trucks")

else:
    print("We  still cant decide")

if people > trucks:
    print("Alright we just take the trucks")
else:
    print("Fine lets stay home then")
