class Competition:
    raise_amount = 1.04

    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def raise_prize(self):
        self.prize = self.prize * Competition.raise_amount

debate = Competition('Debate', 500)
print(debate.raise_amount)
debate.raise_prize()
print(debate.prize)
print(debate.__dict__)
print(Competition.__dict__)
#changing the class's variables changes the instances variables
Competition.raise_amount = 1.08


print(debate.raise_amount)
debate.raise_prize()
print(debate.prize)