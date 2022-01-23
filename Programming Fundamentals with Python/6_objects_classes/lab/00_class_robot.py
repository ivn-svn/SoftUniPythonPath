class Bot:
    def introduce_bot(self):
        return  f"Bot's name is " + self.name
b1 = Bot()
b1.name = "tamagochi"
b1.color = "white"
b1.weight = 30
intro = b1.introduce_bot()
print(intro)