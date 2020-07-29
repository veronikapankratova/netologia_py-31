from datetime import datetime
from application.db import calculate_salary
from application.db.people import get_employees

now = datetime.now()
print('Текущая дата:', now)

if __name__ == '__main__':
    calculate_salary()
    get_employees()