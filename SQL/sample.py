import sqlite3
from employee import Employee

conn = sqlite3.connect('sample.db')

c = conn.cursor()

# c.execute("""
#     CREATE TABLE EMPLOYEES(
#           first text,
#           last text,
#           salary real 
#     )
# """)


# c.execute("""
#     INSERT INTO Employees VALUES("Rahul", "Sarkar", 25000)
# """)

emps = [ 
    Employee("Amit", "Kumar", 30000), 
    Employee("Firoj", "Sekh", 25000),
    Employee("Nilesh", "Roy", 35000)
]

for emp in emps:
    c.execute("""INSERT INTO Employees VALUES(?, ?, ?)""",
              (emp.first, emp.last, emp.salary))

c.execute("""
    SELECT * FROM Employees 
""")

emp_list = c.fetchall()

for first, last, pay in emp_list:
    print(first, last, pay)

conn.commit()
conn.close()
