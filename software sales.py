a=eval(input("Enter the number of packages purchased: "))

if a>100:
    j=(a*99)*0.4
    print("Discount Amount 40% : $" ,format(j,".2f"))
    print("Total Amount: $ ",format((99*a-j),".2f"))
elif 50<=a<=99:
    j = (a * 99) * 0.3
    print("Discount Amount 30% : $", format(j,".2f"))
    print("Total Amount: $ ", format((99 * a - j),".2f"))
elif 20<=a<=49:
    j = (a * 99) * 0.2
    print("Discount Amount 20% : $", format(j,".2f"))
    print("Total Amount: $ ", format((99 * a - j),".2f"))
elif 10<=a<=19:
    j = (a * 99) * 0.1
    print("Discount Amount 10% : $", format(j,".2f"))
    print("Total Amount: $ ",format((99 * a - j),".2f"))
else:
    print("Discount Amount 40 0% : $0.00")
    print("Total Amount: $ ", format((99 * a ),".2f"))