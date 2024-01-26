class Competition:
    participants = []

    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

debate = Competition('Debate', 500)
print(debate.participants)

Competition.participants.append('John')
debate.participants.append('Alice')
print(debate.participants)
print(Competition.participants)

essay = Competition('Essay', 456)
print(essay.participants)
