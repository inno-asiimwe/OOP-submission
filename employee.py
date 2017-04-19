class Employee:

    def __init__(self, Name, id, typ, date):
        self.name = Name
        self.id = id
        self.department = Dept
        self.status = 'current'
        self.type = typ
        self.joiningdate = date

    def resign(self, date):
        self.status = 'resigned'
        self.leavingdate = date

    def __layoff(self, date):
        self.status = 'laid off'
        self.leavingdate = 'date'

    def calculate_pay(self, period):
        raise NotImplementedError("implemented by child classes")

    def needs_Workpermit(self):
        if self.type == 'expatriate':
            return True
        else:
            return False





class permanent_Employee(Employee):

    def __init__(self, Name, id, Dept, typ, office, salary, date):
        Employee.__init__(self, Name, id, typ, date)
        self.department = Dept
        self.office = office
        self.gross = salary




    def shift_office(self, new_office):
        self.office = new_office

    def calculate_pay(self, period):
        if type == 'Expatriate':
            deductions = 0.10 * self.gross
        else:
            deductions = 0.10 * self.gross + 0.05 * self.gross
        return (self.gross - deductions) * period

class contract_Employee(Employee):

    def __init__(self, Name, id, Dept, office, salary, date, contract, allowance, typ = "Expatriate"):
        Employee.__init__(self, Name, id, typ, date)
        self.department = Dept
        self.office = office
        self.gross = salary
        self.contract = contract
        self.allowance = allowance


    def endContract(self,date):
        self.status = 'contract ended'
        self.leavingdate = date

    def calculate_pay(self, period):
        if type == 'Expatriate':
            deductions = 0.10 * self.gross
        else:
            deductions = 0.10 * self.gross + 0.05 * self.gross
        return (self.gross + self.allowance - deductions) * period

class casual_Employee(Employee):

    def __init__(self, Name, id, rate, date, typ = 'local'):
        Employee.__init__(self, Name, id, typ, date)
        self.rate = rate



    def  calculate_pay(self, duration):
        return self.rate * duration
