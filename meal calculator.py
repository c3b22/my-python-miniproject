price = int(input("Enter the price of the meal :"))
print ("\n")
vat = price*7/100
total = vat + price
print ("price of meal :",price)
print ("VAT :",vat)
print ("Total Amount :",total)
print ("\n")
aot = int(input("Enter amount of the tender :"))
print ("\n")
print ("Amout Tender :",aot)
print ("Total Amount :",total)
c = aot - total
print ("change :",c)
