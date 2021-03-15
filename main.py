from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, tzinfo

if __name__ == '__main__':
    print(f'Запуск осуществлеен на: {datetime.now().strftime("%d/%m/%y %H:%M")}')
    calculate_salary()
    get_employees()
