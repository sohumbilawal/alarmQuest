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
    timeOfDay = input("Is this AM(please type am) or PM(please type pm)? or 24-hour format(please type 24)")
    if timeOfDay == "pm" or timeOfDay == "PM":
        inpHour += 12
    else:
        print("We are all good!")
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

alarmDay = 0
while alarmMins > 59: #If someone decides to get cute and put in 8 hours and 34563 minutes of sleep needed, this should take care of it.
    alarmMins -= 60
    alarmHour += 1

print("You will wake up at: ", alarmHour, alarmMins)

while alarmHour > 23:
    alarmHour -= 24
    alarmDay += 1

#This is like pressing the numbers down into sensible proportions that we can undersand.
#Like distillation of a number like 8 hours 354897 minutes into a time and 247 days for example.
if len(str(alarmMins)) == 1:
    alarmMins = "0{}".format(alarmMins)
if alarmHour < 13 and alarmDay > 0:
    print("You will wake up at {}:{} am in {} days".format(alarmHour, alarmMins, alarmDay))

elif alarmHour > 12 and alarmDay > 0:
    alarmHour -= 12
    print("You will wake up at {}:{} pm in {} days".format(alarmHour, alarmMins, alarmDay))

elif alarmHour < 13 and alarmDay == 0:
    print("You will wake up at {}:{} am today".format(alarmHour, alarmMins))

elif alarmHour > 12 and alarmDay == 0:
    print("You will wake up at {}:{} pm today".format(alarmHour, alarmMins))

#print("You will wake up at: ", alarmHour, alarmMins, " in ", alarmDay, " days")
