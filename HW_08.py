from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(1985, 7, 30)},
    {'name': 'Jane', 'birthday': datetime(1995, 7, 8)},
    {'name': 'Bob', 'birthday': datetime(2000, 7, 9)},
    {'name': 'Alice', 'birthday': datetime(2001, 7, 10)},
    {'name': 'David', 'birthday': datetime(1999, 8, 4)},
    {'name': 'Eva', 'birthday': datetime(1997, 8, 5)},
    {'name': 'Mike', 'birthday': datetime(1990, 7, 17)},
    {'name': 'Anna', 'birthday': datetime(1991, 7, 15)},
    {'name': 'Tom', 'birthday': datetime(2002, 7, 12)},
]



def get_birthdays_per_week(users):
    today = datetime.now().date() # Поточна дата
    start_period = today + timedelta(days=(today.weekday() + 1) % 7) # Початок поточного тижня (понеділок)
    end_period = start_period + timedelta(days=6) # Кінець поточного тижня (неділя)
    start_of_week = start_period + timedelta(days=2)

    # weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    congrats = {}

    # for i in range(7):
    #     current_day = start_of_week + timedelta(days=i) # Поточний день в межах тижня 
    #     if current_day <= end_of_week: # Перевірка, чи день належить поточному тижню
    #         print(weekdays[i] + ':', end=' ')
    #         if i < 5: # Робочий день
    for user in users:
        birthday = user['birthday'].date().replace(year=today.year)
        if start_period <= birthday <= end_period:
            # print(user['name'], end=', ')
            if birthday.weekday() in (5, 6):
                birthday = start_of_week
            if congrats.get(birthday):
                congrats[birthday].append(user['name'])
            else:
                congrats[birthday] = [user['name']]
            # else: # Вихідний день
            #     monday = start_of_week + timedelta(days=7)
            #     for user in users:
            #         birthday = user[ 'birthday'].date()
            #         if (birthday.day == current_day.day and birthday.month == current_day.month) or (birthday > current_day and birthday.weekday() < 5):
            #             print(user['name'], end=', ')
            #     if monday.month == current_day.month and current_day.weekday() == 6:
            #         for user in users:
            #             birthday = user['birthday'].date()
            #             if birthday.weekday() < 5 and birthday > current_day and birthday < monday:
            #                 print(user['name'], end=', ')
            # print()
    for bd, users in congrats.items():
        print(f'{bd.strftime("%A")}: {", ".join(users)}')
            


if __name__ == "__main__":
    get_birthdays_per_week(users)









