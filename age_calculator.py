# Enter year of birth: 2000
# Enter month of birth: 6
# Enter day of birth: 6
# You are 18 years old.

from datetime import date
import datetime


def get_dob(birthyear, birthmonth, birthday):

    birthyear = int(input("Enter year of birth: "))
    birthmonth = int(input("Enter month of birth: "))
    birthday = int(input("Enter day of birth: "))
    dob = datetime.date(birthyear, birthmonth, birthday)
    return dob


def get_age(dob):
    today = date.today()
    age = today.year - dob.year

    return age


def main():
    dob = get_dob(2000, 6, 6)
    age = get_age(dob)
    today = date.today()

    if dob > today:
        print("You are not born yet.")
    else:
        print("You are", age, "years old.")


if __name__ == '__main__':
    main()
