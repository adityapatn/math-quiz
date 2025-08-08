#the purpose of this program is to generate random numbers that test the user's speed and accuracy of computing mathematical operations like addition, subtraction, multiplication, and division.
import random
import time

var_dict = {
    "symbol":{
        "a": "+",
        "s":"-",
        "m":"*",
        "d":"/"
    }
}

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
questions = 5 #int(input("Number of questions: "))
op = "a" #input("Enter an operation: a|s|m: ")
digits = 1 #int(input("Enter the number of digits: "))

#internal variables
question_num = 0 #is 1 when loop starts
total_correct = 0
total_time = 0

countdown()

while question_num < questions:
        num_a = random.randint(10 ** (digits - 1), 10 ** (digits) - 1)
        num_b = random.randint(10 ** (digits - 1), 10 ** (digits) - 1)
        answer = num_a + num_b

        print("\nQuestion", question_num + 1)
        print(num_a, var_dict["symbol"][op], num_b)
        start_time = time.time()
        attempt = input("Answer: ")
        end_time = time.time()
        question_num += 1 #a question has been answered
        if attempt == "exit":
            break
        else:
            attempt = int(attempt)
        elapsed_time = end_time - start_time
        total_time += elapsed_time
        if attempt == answer:
            total_correct += 1

avg_time = round(total_time / question_num, 2)
print("Average time:", avg_time, "s")
print("Number correct:", total_correct, "out of", question_num)
prcnt_correct = round(total_correct / question_num, 3) * 100
print("Percent correct:", prcnt_correct)
combined_score = round(prcnt_correct * (1.5 / avg_time), 2)
print("\nCombined score:", combined_score)