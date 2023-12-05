from logic import allLogic
from data import questionData

def mainlogic():
    logic = allLogic()
    logic.set_sub_quest(questionData)
    logic.process_sub_quest()

mainlogic()





