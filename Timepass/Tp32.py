class Quiz:
    def __init__(self):
        self.questions = {
            "2+2": "4",
            "3+3": "6"
        }

    def start(self):
        score = 0
        for q, ans in self.questions.items():
            user = input(q + ": ")
            if user == ans:
                score += 1
        print("Score:", score)

q = Quiz()
q.start()
