from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(2023, 6, 30)},
    {'name': 'Jane', 'birthday': datetime(2023, 7, 1)},
    {'name': 'Bob', 'birthday': datetime(2023, 7, 2)},
    {'name': 'Alice', 'birthday': datetime(2023, 7, 3)},
    {'name': 'David', 'birthday': datetime(2023, 7, 4)},
    {'name': 'Eva', 'birthday': datetime(2023, 7, 5)},
    {'name': 'Mike', 'birthday': datetime(2023, 7, 6)},
    {'name': 'Anna', 'birthday': datetime(2023, 7, 7)},
    {'name': 'Tom', 'birthday': datetime(2023, 7, 8)},
]



def get_birthdays_per_week(users):
    today = datetime.now().date() # Поточна дата
    start_of_week = today - timedelta(days=(today.weekday() + 1) % 7) # Початок поточного тижня (понеділок)
    end_of_week = start_of_week + timedelta(days=6) # Кінець поточного тижня (неділя)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(7):
        current_day = start_of_week + timedelta(days=i) # Поточний день в межах тижня 
        if current_day <= end_of_week: # Перевірка, чи день належить поточному тижню
            print(weekdays[i] + ':', end=' ')
            if i < 5: # Робочий день
                for user in users:
                    birthday = user['birthday'].date()
                    if birthday.day == current_day.day:
                        print(user['name'], end=', ')
            else: # Вихідний день
                monday = start_of_week + timedelta(days=7)
                for user in users:
                    birthday = user[ 'birthday'].date()
                    if (birthday.day == current_day.day and birthday.month == current_day.month) or (birthday > current_day and birthday.weekday() < 5):
                        print(user['name'], end=', ')
                if monday.month == current_day.month and current_day.weekday() == 6:
                    for user in users:
                        birthday = user['birthday'].date()
                        if birthday.weekday() < 5 and birthday > current_day and birthday < monday:
                            print(user['name'], end=', ')
            print()


get_birthdays_per_week(users)









