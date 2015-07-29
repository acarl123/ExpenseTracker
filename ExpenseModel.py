import shelve


class ExpenseModel:
    def __init__(self):
        self.reportDict = shelve.open('reports.asft')
        self.addInfoDict = {}