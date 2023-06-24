from datetime import datetime as dt


def calculate_salary():
    print(f'At {dt.now().strftime("%d/%m/%Y, %H:%M:%S")} '
          'calculate_salary was called.')
