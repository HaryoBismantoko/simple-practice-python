class allLogic:
    def __init__(self):
        self.sub_quest = {}
    def set_sub_quest(self,data):
        self.sub_quest = data
    def process_sub_quest(self):
        score = 0
        for items in self.sub_quest:
            text = items.get('text')
            answer = items.get('answer')
            print(text)
            inp_quest = input("true / false : ")
            if inp_quest.lower() == answer.lower():
                print("Answer is right")
                score += 1
                print(f"Your score is {score}")
            else:
                print("Answer is wrong")

        print(f"\n \033[1mYour final score is {score}\033[0m")


