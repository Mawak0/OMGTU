def dif_dates(date1_str, date2_str):
    def next_day(date):
        if date[2] % 4 == 0:
            months[1] = 29
        else:
            months[1] = 28
        if months[date[1]-1] > date[0]:
            date[0] += 1
            return date
        elif date[1] < 12:
            date[1] += 1
            date[0] = 1
            return date
        else:
            date[2] += 1
            date[0] = 1
            date[1] = 1
            return date
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 28 >> 29 високосный
    date1 = [int(i) for i in date1_str.split(".")] # day1, month1, year1
    date2 = [int(i) for i in date2_str.split(".")]
    days = 1
    while date1 != date2:
        date1 = next_day(date1)
        days += 1
    return days


date1_str = input()
date2_str = input()
p = int(input())
days = dif_dates(date1_str, date2_str)
rez = p
for i in range(1, days):
    rez += p+i
print(rez)