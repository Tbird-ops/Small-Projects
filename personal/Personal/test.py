class Agent():
    name = ''
    hot_drink = ''
    cases_total = 0
    cases_solved = 0

    def __init__(self, name, hot_drink, cases_total, cases_solved):
        self.name = name
        self.hot_drink = hot_drink
        self.cases_total = cases_total
        self.cases_solved = cases_solved

    def speak(self, speech):
        print(self.name + ' says: "' + speech + '"')

    def drink(self):
        print(self.name + ' drinks a cup of ' + self.hot_drink + '.')

    def get_total_cases(self):
        print(self.name + ' has a total of ' + str(self.cases_total) + ' cases.')

    def add_new_case(self, number):
        self.cases_total += number
        if (number > 1):
            print(self.name + ' has been given ' + str(number) + ' new cases.')
        else:
            print(self.name + ' has been given ' + str(number) + ' new case.')

    def get_solved_cases(self):
        print(self.name + ' has solved ' + str(self.cases_solved) + ' cases.')

    def solve_case(self, number):
        self.cases_solved += number
        if (number > 1):
            print(self.name + ' has solved ' + str(number) + ' cases, wow!')
        else:
            print(self.name + ' has solved a case, great job!')
    
agent_q = Agent('Agent Q', 'decaf coffee', 20, 12)

agent_q.speak("Hi, I'm Agent Q!")

agent_q.get_total_cases()
agent_q.add_new_case(2)
agent_q.get_total_cases()

agent_q.get_solved_cases()
agent_q.solve_case(1)
agent_q.get_solved_cases()