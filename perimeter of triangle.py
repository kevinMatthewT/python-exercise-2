s1=eval(input("Enter length of edge1:"))
s2=eval(input("Enter length of edge2:"))
s3=eval(input("Enter length of edge3:"))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print("The perimeter is", (s1+s2+s3))
else:
    print("Perimeter cannot be calculated: the input is invalid.")