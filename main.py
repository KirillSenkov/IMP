from application import salary
from application.db.people import get_employees as ge

if __name__ == '__main__':
    salary.calculate_salary()
    ge()
