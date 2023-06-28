from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(2023, 6, 26)},
    {'name': 'Jane', 'birthday': datetime(2023, 6, 27)},
    {'name': 'Bob', 'birthday': datetime(2023, 6, 28)},
    {'name': 'Alice', 'birthday': datetime(2023, 6, 29)},
    {'name': 'David', 'birthday': datetime(2023, 6, 30)},
    {'name': 'Eva', 'birthday': datetime(2023, 7, 1)},
    {'name': 'Mike', 'birthday': datetime(2023, 7, 2)},
]



def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(7):
        current_day = start_of_week + timedelta(days=i)
        if current_day <= end_of_week:
            print(weekdays[i] + ':', end=' ')
            for user in users:
                if user['birthday'].date() == current_day and current_day.weekday() < 5:
                    print(user['name'], end=', ')
            print()


get_birthdays_per_week(users)

