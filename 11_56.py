# wait for my comeback after thesis ey.
# Create a program that asks for a user input with if-else.
# input() is for scanner.
xh = input("Enter the value of X: ")
ih = int(xh)
x = ih
# Use switch or if-else for the problem.
if x < 2 :
    print("Small")
elif x < 10 :
    print("Medium")
else : 
    print("Large")
print("All Done")

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
