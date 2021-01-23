# working with DATE
from datetime import date
from datetime import timedelta
from datetime import datetime

import calendar


class Clock():
    days = ['Monday', 'Thuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    now = datetime.now()
    today = date.today()
    curr_time = datetime.time(now)

    def get_yesterday(self):
        print('Yesterday:', str((self.now) - timedelta(days=1)))

    def get_tommorow(self):
        print('Tommorrow:', str(self.now + timedelta(days=1)))

    def get_next_year(self):
        print('One year from now will be:', str(self.now + timedelta(days=365)))

    def formated_time(self):
        print(self.now.strftime('Current time: %I:%M:%S %p'))
        print(self.now.strftime('24-hour time: %H:%M'))

    def get_locale_info(self):
        print(self.now.strftime('The local date and time: %c'))
        print(self.now.strftime('The local date: %x'))
        print(self.now.strftime('The local time: %X'))

    def get_formated_data(self):
        print(self.now.strftime('The current year is: %Y'))
        print(self.now.strftime('The current day is: %A'))
        print(self.now.strftime('The current month is: %B'))
        print(self.now.strftime('The current day of month: %d'))

    def main(self):
        print('Today date is:', self.today)
        print('Date components:', self.today.day, self.today.month, self.today.year)
        print('Today weekday:', self.days[self.today.weekday()])
        print('Timestamp:', self.now)
        print('Time is:', self.curr_time)


clock = Clock()

clock.main()

clock.get_formated_data()
clock.get_locale_info()
clock.formated_time()
clock.get_next_year()
clock.get_tommorow()
clock.get_yesterday()

# working with calendar
c = calendar.TextCalendar(calendar.MONDAY)
ct = c.formatmonth(2021, 1, 0, 0)
print(ct)

# HTML CALENDAR
hc = calendar.HTMLCalendar(calendar.MONDAY)
ht = hc.formatmonth(2021, 1)
print(ht)

# iterate thrue days august 2021
for i in c.itermonthdays(2021, 8):
    print(i)

# iterate thue weekdays
for day in calendar.day_name:
    print(day)

print('First friday fuck of the month will be:')
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY] != 0:
        fuckday = weekone[calendar.FRIDAY]
    else:
        fuckday = weektwo[calendar.WEDNESDAY]

    print('%10s %2d' % (calendar.month_name[m], fuckday))
