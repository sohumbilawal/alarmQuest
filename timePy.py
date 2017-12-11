#This will have 2 user inputs: One is time in HH:MM and another is similar HH:MM
#input that tells when the alarm in the future is supposed to go off
currentTime = input("What is the time to count from (in HH:MM): ")

n = 0
for n in range(0, len(currentTime)):
    if currentTime[n] == ":":
        inpHourS = currentTime[0:n]
        inpMinsS = currentTime[n+1:]
        inpHour = int(inpHourS)
        inpMins = int(inpMinsS)
#for chars in currentTime:
#    if chars == ":":
#        print("Please include : and use the format HH:MM.")
#    else:
#        print("Invalid entry.")

if inpMins > 59:
    print("Invalid entry. Minutes cannot be more than 59.")

if inpHour > 23:
    print("Invalid entry.")
elif inpHour > 12:
    print("Time is in 24-hour format.")
elif inpHour < 0:
    print("Invalid entry.")
elif inpHour < 12:
    timeOfDay = input("Is this AM(please type am) or PM(please type pm)?")
    if timeOfDay == "pm":
        inpHour += 12

print("Current Time: ", inpHour, inpMins)

targetTime = input("How long do you want to sleep? (in HH:MM): ")

n = 0
for n in range(0, len(targetTime)):
    if targetTime[n] == ":":
        tarHourS = targetTime[0:n]
        tarMinsS = targetTime[n+1:]
        tarHour = int(tarHourS)
        tarMins = int(tarMinsS)

print("Target time: ", tarHour, tarMins)

alarmHour = inpHour + tarHour
alarmMins = inpMins + tarMins

if alarmMins > 59:
    alarmMins -= 60
    alarmHour += 1
print("You will wake up at: ", alarmHour, alarmMins)
