from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(1985, 7, 14)},
    {'name': 'Jane', 'birthday': datetime(1995, 7, 15)},
    {'name': 'Bob', 'birthday': datetime(2000, 7, 13)},
    {'name': 'Alice', 'birthday': datetime(2001, 7, 10)},
    {'name': 'David', 'birthday': datetime(1999, 8, 4)},
    {'name': 'Eva', 'birthday': datetime(1997, 8, 5)},
    {'name': 'Mike', 'birthday': datetime(1990, 7, 11)},
    {'name': 'Anna', 'birthday': datetime(1991, 7, 16)},
    {'name': 'Tom', 'birthday': datetime(2002, 7, 12)},
]

def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    start_period = current_datetime + timedelta(days=(7 - current_datetime.weekday() + 1) % 7)
    end_period = start_period + timedelta(days=6)
    start_of_week = start_period

    congrats = {}

    for user in users:
        birthday = user['birthday'].date().replace(year=current_datetime.year)
        if start_period.date() <= birthday <= end_period.date():
            if birthday.weekday() >= 5:
                birthday = start_of_week.date()
            if congrats.get(birthday):
                congrats[birthday].append(user['name'])
            else:
                congrats[birthday] = [user['name']]

    sorted_dates = sorted(congrats.keys())
    result = []

    for bd in sorted_dates:
        result.append(f'{bd.strftime("%A")}: {", ".join(congrats[bd])}')

    return result

if __name__ == "__main__":
    birthdays_per_week = get_birthdays_per_week(users)
    for bd in birthdays_per_week:
        print(bd)
