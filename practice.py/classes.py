class Employee:
    num_of_empys=0
    raise_amount= 1.04
    def __init__(self,first,last,phone,email,pay):
        self.first=first
        self.last=last
        self.phone=phone
        self.email=email
        self.pay=pay
    def full_name(self):
        return f"{self.first}{self.last}"
    def apply_raise(self):
        self.pay=int(float(self.pay)* 1.04)
Employee.num_of_empys+=1
print(Employee.num_of_empys)
emp_1= Employee('Jag','Singh','6127071406','jag.singh@gmail.com','60000')
emp_2= Employee("Kanwal","Kaur","6514001211","kanwal.kaur@compant.com","60000")
Employee.num_of_empys+=1
print(Employee.num_of_empys)


emp_2.raise_amount=1.05

print(emp_1.first)
print(emp_1.last)
print(emp_1.phone)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.full_name())