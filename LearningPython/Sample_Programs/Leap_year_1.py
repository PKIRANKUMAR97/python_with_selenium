year = int(input())


def is_leap(year):
    leap = False
    if (year%4) == 0:
        print("True")
    elif (year % 400) == 0 and (year % 100) == 0:
        print("True")
    elif (year % 4) == 0 and (year % 100) != 0:
        print(leap)
    else:
       print("False")
    return ''


print(is_leap(year))
