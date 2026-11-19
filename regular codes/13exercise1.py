from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S") # H - hour, M- minute, S - second
print("Current Time =", current_time)

if ("12" >="%H" and "%H">="0" ):
    print("Good Morning")
elif ("17" >="%H" and "%H">="12"):
    print("Good Afternoon")
elif ("20" >="%H" and "%H">="17"):
    print("Good Evening")
else:
    print("Good Night")        




from datetime import datetime, date, timedelta

now = datetime.now()              # current date and time
today = date.today()              # current date
tomorrow = today + timedelta(days=1)

print(now)
print(today)
print(tomorrow)