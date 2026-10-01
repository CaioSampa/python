def helper_recursive(day, end):
    if(end + 1 == day):
        return print("Harvest time!")
    else:
        print("Day", day)
    day += 1
    helper_recursive(day, end)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper_recursive(1, days)
