from datetime import datetime as dt


def get_employees():
    print(f'At {dt.now().strftime("%d/%m/%Y, %H:%M:%S")} '
          'get_employees was called.')