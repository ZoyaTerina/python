import playsound
import random
class MusicBox:
    def __init__(self):
        self.variants = "OLM"     # варианты угадываемых букв
        self.score = 0  # очки
        self.sequence = random.choice(self.variants)  # последовательность вариантов
    def __next(self):
        dlina = len(self.sequence) + 1   # прибавляем к длине
        self.sequence = " "
        for _ in range(dlina):
            self.sequence += random.choice(self.variants)
    def proverit(self, otvet):
        if otvet == self.sequence:
            playsound.playsound("sounds/correct.wav")
            self.__next()
            self.score +=1
        else:
            playsound.playsound("sounds/incorrect.wav")
            self.score -= 0.5
    def igraem(self):
        for letter in self.sequence:
            playsound.playsound(f"sounds/{letter}.mp3")


















































