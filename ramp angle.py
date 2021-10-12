
import math
m=eval(input("Enter the mass of the cart (in kg):"))
f=eval(input("Enter the force to push the cart (in N):"))

a=(f/(9.8*m))


print("The angle of the ramp is" ,round(math.degrees(math.asin (a)),1) , "degrees")