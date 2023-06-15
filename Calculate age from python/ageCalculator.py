from datetime import datetime
import calendar

now=datetime.now()
y=now.strftime('%Y')
m=now.strftime('%m')
d=now.strftime('%d')

b_year=int(input('Birth year: '))
b_month=int(input('Birth month: '))
b_date=int(input('Birth date: '))
print('------------------------')

c_y=int(y)
c_m=int(m)
c_d=int(d)

print('Current year: ',c_y)
print('Current month: ',c_m)
print('Current date: ',c_d)
print('------------------------')
    

if b_year>c_y or b_month>12 or  b_date>calendar.monthrange(c_y, c_m)[1]:
    print('Invalid birth information!')

elif c_m<b_month:
    year =  c_y-b_year-1
    if c_d<b_date:
        month =  12-b_month+c_m-1
        days =  c_d+ calendar.monthrange(c_y, c_m-1)[1]-b_date
        print(f'You are {year} years, {month} month and {days} days old.')
    else:
        month =  12-b_month+c_m
        days =  c_d-b_date
        print(f'You are {year} years, {month} month and {days} days old.')

elif c_m==b_month:
    if c_d<b_date:
        year = c_y-b_year-1
        month =  12-b_month+c_m-1
        days = c_d+ calendar.monthrange(c_y, c_m-1)[1]-b_date
        print(f'You are {year} years, {month} month and {days} days old.')

    elif c_d>=b_date:
        year = c_y-b_year
        month = c_m-b_month
        #or we can simply write 0 month
        days =  c_d-b_date
        print(f'You are {year} years, {month} month and {days} days old.')
    
else:
    year =  c_y-b_year
    if c_d>=b_date:
        month = c_m-b_month
        days =  c_d-b_date
        print(f'You are {year} years, {month} month and {days} days old.')
    else:
        month = c_m-b_month-1
        days =  c_d+ calendar.monthrange(c_y, c_m-1)[1]-b_date
        print(f'You are {year} years, {month} month and {days} days old.')
    

