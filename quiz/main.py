from data import question_data
score = 0
for quesAsk in question_data:
    for key, value in quesAsk.items():
        if key == 'text':
            print(value)
        elif key == 'answer':
            answer = value
            inpQuest = input("true / false : ")
            if inpQuest.lower() == answer.lower():
                print("Answer is right")
                score +=1
                print(f"Your score is {score}")
            elif inpQuest.lower() != answer.lower():
                print("Answer is wrong")

print(f"\n \033[1mYour final score is {score}\033[0m")




