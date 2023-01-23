import math
# Ask the user to from the question
# if the answer is correct print out true
# if else print out incorrect!!! try again
#



print("Mathematics Quiz")
question1 = "Who is femi?"
options1 = "a.Boy\nb. Girl \nc. Non Living Thing\n"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', 'b', or 'c' for your answer\n")

    if response == "a":
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = input("Hit 'a', 'b', or 'c' for your answer\n")

            if response == "a":
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break

question2 = "How old is femi?"
options1 = "a.13\nb. 22 \nc. 100\n"
print(question1)
print(options1)

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "c":
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "c":
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")