#This will have 2 user inputs: One is time in HH:MM and another is similar HH:MM
#input that tells when the alarm in the future is supposed to go off

#So we start with the first input here, the currentTime, or the startTime,
#call it what you will. I find starting with baby steps helps the most.
currentTime = input("What is the time to count from (in HH:MM): ")

#Instead of keeping the basic processing of the input to later, we do it right
#here. As you can see, I am struggling with trying to detect an invalid input.

#But what we have done here is using string slicing/ modification, we create
#hours and minutes variables, so we can make the computer understand time.

n = 0 #Pretty sure this is unnecessary in Python, but old C++ habits die hard.
for n in range(0, len(currentTime)):
    if currentTime[n] == ":":
        inpHourS = currentTime[0:n]
        inpMinsS = currentTime[n+1:]
        inpHour = int(inpHourS) #Converting to int for processing later
        inpMins = int(inpMinsS)

#for chars in currentTime:
#    if chars == ":":
#        print("Please include : and use the format HH:MM.")
#    else:
#        print("Invalid entry.")

#Logic related to numbers that were just strings for Python.

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

#This is something I love to do: keep printing stuff out. Track your variables.
#We do not have a Matlab style console/ editor. So we make do with prints.
print("Current Time: ", inpHour, inpMins)

targetTime = input("How long do you want to sleep? (in HH:MM): ")

n = 0
for n in range(0, len(targetTime)):
    if targetTime[n] == ":":
        tarHourS = targetTime[0:n]
        tarMinsS = targetTime[n+1:]
        tarHour = int(tarHourS)
        tarMins = int(tarMinsS)

#We will not need the same kidn of logic, since it is mentioned that users of
#this app might have to sleep 92 hours and such. Oh well.
print("Target time: ", tarHour, tarMins)

alarmHour = inpHour + tarHour
alarmMins = inpMins + tarMins

if alarmMins > 59:
    alarmMins -= 60
    alarmHour += 1

print("You will wake up at: ", alarmHour, alarmMins)
