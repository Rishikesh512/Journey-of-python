class Cricket:
    def __init__(self):
        self.runs = 0
        self.wickets = 0
        self.overs = 0

    def add_runs(self, runs):
        self.runs += runs

    def add_wicket(self):
        self.wickets += 1

    def add_over(self):
        self.overs += 1

    def show_score(self):
        print(f"Score: {self.runs}/{self.wickets} in {self.overs} overs")


c = Cricket()
c.add_runs(4)
c.add_runs(6)
c.add_wicket()
c.add_over()

c.show_score()
