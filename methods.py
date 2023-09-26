class Employee:
    num_of_emp = 0
    raise_amount = 2.04
    def __init__(self, first, last, pay, email):
        self.first = first
        self.last = last
        self.first = first
        self.pay = pay
        self.email = email

        Employee.num_of_emp += 1

    def fullname(self):
        return f' {emp_1.first} {emp_1.last}'
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
      
        
    
emp_1 = Employee('vic','wanjala',60000,'vic@gmail.com')
emp_2 = Employee('Jon','wanjala',6000,'jon@gmail.com')
emp_2 = Employee('Jz','Tes',40000,'res@gmail.com')
import datetime
my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))

Employee.set_raise_amount(1.50)
print(Employee.raise_amount)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.num_of_emp)