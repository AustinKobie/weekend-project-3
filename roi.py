# first we are going to create a class for each sections of the roi program.
# these being Income, Expenses, Cash Flow and Cash on Cash ROI.
# Cash Flow is going to be Income minus Expenses, this will give us the total monthly cash flow.
class Roi:
    
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.cash_roi = 0

    def get_income(self):
        self.income = float(input("please enter your monthly projected income: "))
        
    def get_expenses(self):
        tax = float(input("what are your monthly tax expenses: "))
        insurance = float(input("what are your monthly insurance expenses: "))
        utilities = float(input("what are your monthly utility expenses: "))
        hoa = float(input("what are your monthly hoa expenses: "))
        lawn = float(input("what are your monthly lawn expenses: "))
        vacancy = float(input("what are your monthly vacancy expenses: "))
        repairs = float(input("what are your monthly repair expenses: "))
        cap_ex = float(input("what are your monthly capital expense: "))
        property_managment = float(input("what are your monthly management expenses: "))
        mortgage = float(input("what are your monthly mortgage expenses: "))
        
        self.expenses = tax + insurance + utilities + hoa + lawn + vacancy + repairs + cap_ex + property_managment + mortgage 
    
    def calculate_cashflow(self):
        self.cashflow = self.income - self.expenses
        print (f"total cashflow is {self.cashflow}")  
        
        self.cashflow *= 12 

    
        
        
        
    def get_cash_roi(self):
        down_payment = float(input("what is your down payment on the property? "))
        closing_costs = float(input("what is your closing cost on the property? "))
        rehab_budget = float(input("what is your rehab budget on the property? "))
        misc_other = float(input("what is your misc cost on the property? "))

        self.cash_roi = down_payment + closing_costs + rehab_budget + misc_other
        cash_on_cash_roi = self.cashflow/self.cash_roi 
        cash_on_cash_roi *= 100
        print(f"Cash on cash ROI: {cash_on_cash_roi}%")

    
    
    
    
roi = Roi()
roi.get_income()
roi.get_expenses()
roi.calculate_cashflow()
roi.get_cash_roi()



