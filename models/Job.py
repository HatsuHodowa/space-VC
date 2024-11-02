class Job:
    def __init__(self, title, income):
        self.title = title
        self.income = income
    
    def to_dict(self):
            return {
                "title": self.title,
                "income": self.income,
            }
