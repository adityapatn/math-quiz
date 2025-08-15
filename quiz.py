#the purpose of this program is to generate random numbers that test the user's speed and accuracy of computing mathematical operations like addition, subtraction, multiplication, and division.
import random
import time
import sys
import math

def countdown():
    print("3..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    time.sleep(1)
    print("Go!")
    time.sleep(1)

#user-modifiable variables
print("Welcome to Math Quiz!")
questions = int(input("Number of questions (answer exit to quit early): "))
op = input("Enter an operation (a|s|m|d): ")
digits_1 = int(input("Enter the number of digits in the first number (dividend for division): "))
digits_2 = int(input("Enter the number of digits in the second number (divisor for division): "))
if digits_1 < digits_2: #prevent errors in division
    digits_1 = digits_2 + 1

#confirmed that digit and question count variables work as expected
#confirmed that number generation for division works as expected

#internal variables
question_num = 0 #is 1 when loop starts
total_correct = 0
total_time = 0

max_time = 5 * (digits_1 + digits_2)
digit_min_1 = 10 ** (digits_1 - 1)
digit_max_1 = 10 ** (digits_1) - 1
digit_min_2 = 10 ** (digits_2 - 1)
digit_max_2 = 10 ** (digits_2) - 1

countdown()

while question_num < questions:
        
        match op:
            case "a":
                symbol = "+"
                num_a = random.randint(digit_min_1, digit_max_1)
                num_b = random.randint(digit_min_1, digit_max_2)
                answer = num_a + num_b
            case "s":
                symbol = "-"
                num_a = random.randint(digit_min_1, digit_max_1)
                num_b = random.randint(digit_min_2, digit_max_2)
                answer = num_a - num_b
            case "m":
                symbol = "*"
                num_a = random.randint(digit_min_1, digit_max_1)
                num_b = random.randint(digit_min_2, digit_max_2)
                answer = num_a * num_b
            case "d":
                symbol = "/"
                num_2 = random.randint(digit_min_2, digit_max_2) #this is the divisor
                num_1 = random.randint(math.ceil(digit_min_1 / num_2), math.floor(digit_max_1 / num_2)) #we need to limit this number so that the product num_1 * num_2 conforms to digits_1

                num_a = num_1 * num_2 #this is our dividend, must conform to digits_1
                num_b = num_2 #this is our divisor, must conform to digits_2
                answer = num_1

        print("Question", question_num + 1)
        print(num_a, symbol, num_b)
        start_time = time.time()
        #print(answer) #for testing purposes
        try:
            attempt = input("Answer: ")
        except KeyboardInterrupt:
            print("\n")
            break
        print("")
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

        if attempt == "exit":
            break
        else:
            question_num += 1 #a question has been answered
            try:
                attempt = int(attempt)
            except ValueError: #count it as incorrect
                attempt = answer + 1
            if attempt == answer:
                total_correct += 1
                print("Correct!\n")
            else:
                print("Incorrect.\n")

def print_scores():
    avg_time = round(total_time / question_num, 2)
    print("Average time:", str(avg_time) + "s")

    print("Number correct:", total_correct, "out of", question_num)
    prcnt_correct = round(total_correct / question_num, 4) * 100
    print("Percentage correct:", str(prcnt_correct) + "%")

    speed_score = max(0, 100 * (1 - avg_time / max_time)) #normalize avg_time to 0-100
    combined_score = round(0.7 * prcnt_correct + 0.3 * speed_score, 2) #weighted combined scoring

    #combined_score = round(prcnt_correct * (1.5 / avg_time), 2)
    print("Combined score:", combined_score)

if question_num == 0:
    print("Answer at least one question to view your score.")
    sys.exit()
else:
    print_scores()