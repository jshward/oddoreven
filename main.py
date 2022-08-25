print("Is a number odd or even?")

print()

print("Enter the number zero to exit.")

numb = 1



while numb != 0:

    number = input("What number would you like to check?")
    numb = int(number) 

    if numb == 0:
        print("Goodbye")
        break

    elif numb % 2  == 0:
        print("That number is even")



    else:
        print("That number is odd")

