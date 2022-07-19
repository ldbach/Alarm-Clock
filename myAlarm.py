import datetime

alarmHour = int(input("What hour do you want to wake up? "))
alarmMinute = int(input("What minute do you want to wake up? "))
amPm = str(input("am or pm? "))
validTime = False
# checks to see if the user has entered in a valid hour
def check_hour_input(alarmHour, alarmMinute, amPm):
    if alarmHour <= 12 and alarmHour > 0 and alarmMinute < 60 and alarmMinute >= 0:
        if amPm == "am" or amPm == "pm":
            validTime = True
    return validTime

while (validTime == False):
    print("The time does not exist. Please try again. ")
    alarmHour = int(input("What hour do you want to wake up? "))
    alarmMinute = int(input("What minute do you want to wake up? "))
    amPm = str(input("am or pm? "))
    if (check_hour_input(alarmHour, alarmMinute, amPm) == True):
        validTime = True

if (amPm == "pm"):
    alarmHour = alarmHour + 12

while (True):
    if (alarmHour == datetime.datetime.now().hour and
        alarmMinute == datetime.datetime.now().minute):
        print("Wake up, sir")
        break

print("existed")