import logging

# logging.basicConfig(
#     filename="log.log",
#     filemode="w",
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG
# )

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("Employee.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info(f"Employee Created : {self.name}, email - {self.email}")

    @property
    def email(self):
        return "{}{}@gmail.com".format(self.first, self.last)
    
    @property
    def name(self):
        return f"{self.first} {self.last}" 

a = Employee("ankan", "debnath")

# print(a.email)