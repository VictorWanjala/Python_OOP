class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay, email):
        self.first = first
        self.last = last
        self.first = first
        self.pay = pay
        self.email = email


    def fullname(self):
        return f' {self.first} {self.last}'
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.24

    def __init__(self, first, last, pay, email,prog_lang):
        super().__init__(first, last, pay, email)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amount = 1.50
    def __init__(self, first, last, pay, email,employees = None):
        super().__init__(first, last, pay, email)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print( emp.fullname())



dev_1 = Developer('Vic', 'Wanjala', 590000,'vic@gmail.com','python')
dev_2 = Developer('Nic', 'Musula', 50000, 'nic@gmail.com','JS')

# print(dev_1.fullname())
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith',90000, 'mgr@gmail.com',[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()