import datetime

current_date=datetime.datetime.today().date()
current_time=datetime.datetime.today().time()
current_datetime=datetime.datetime.today()
print(current_date)
print(current_time)
print(current_datetime)

filename=current_datetime.strftime('%Y-%m-%d-%H-%M-%S') # will be conerted into this format
filename2=current_datetime.strftime('%Y%m%d%H%M%S') # will be conerted into this format
print(filename)
print(filename2)