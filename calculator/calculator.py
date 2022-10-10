class Calculator:
    def __init__(self, calservice):
        self.calservice = calservice

    def add(self, a, b):
        return self.calservice.add(a, b)