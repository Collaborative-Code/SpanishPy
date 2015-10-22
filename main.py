import random

def main():
    numbers = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

    quiz_length = int(input("How many questions would you like: "))
    right = 0
    for i in range(quiz_length):
        question = random.randint(0, len(numbers) - 1)
        coin = random.randint(0, 50)
        if coin < 25:
            answer = int(input("What number is " + numbers[question] + ": "))
            if answer == question:
                right += 1
        else:
            answer = raw_input("What is " + str(question) + " in spanish: ")
            if answer == numbers[question]:
                right += 1
    print("You got a " + str((right / quiz_length) * 100) + "% of the questions right")
main()
