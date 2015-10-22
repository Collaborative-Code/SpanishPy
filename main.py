import random

from random import shuffle


def main():
    numbers = [
                "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"
              ]

    quiz_length = number_of_questions(numbers)
    right = 0

    test = [i for i in range(quiz_length)]

    shuffle(test)

    for num in test:
        coin = random.randint(0, 50)
        if coin < 25:
            answer = int(input("What number is " + numbers[num] + ": "))
            if answer == num:
                right += 1
            else:
                print("WRONG!")
        else:
            answer = str(raw_input("What is " + str(num) + " in spanish: "))
            if answer == numbers[num]:
                right += 1
            else:
                print("WRONG!")
    print("You got a " + str((right / len(test)) * 100) + "% of the questions right")


def number_of_questions(test_bank):
    user_input = int(input("How many questions would you like: "))
    if user_input > len(test_bank):
        print("Please enter a number between 1 and " + str(len(test_bank)))
        user_input = number_of_questions(test_bank)
    return user_input


main()
