ta=eval(input("Enter the temperature in Fahrenheit: "))

if -58>ta or ta>41 :
    while -58>ta or ta>41:
        print("Temperature must be between -58F and 41F")
        ta=eval(input("Please re-enter the temperature in Fahrenheit: "))

v=eval(input("Enter the wind speed miles per hour:"))

if v<2:
    while v<2:
        print("Speed must be greater than or equal to 2")
        v=eval(input("Please re-enter the wind speed miles per hour:"))

twc=(35.74+(0.6215*ta)-(35.75*(v**0.16))+0.4275*ta*(v**0.16))

print("The wind chill index is",format(twc,".3f"))

