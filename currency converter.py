#Intro about the program
print("This is a program of money converter, and this program will convert 8 most tradable currencies into INR(Indian Rupees)")
print('')

#Now showing list of currencies you want to convert
print('''The following are the most tradable currencies in the world
1>> U.S.Dollasr(USD)
2>> European Euro (EUR)
3>> Japanese Yen (JPY)
4>> British Pound (GBP)
5>> Swiss Franc (CHF)
6>> Canadian Dollar (CAD)
7>> Australian/New Zealand Dollar (AUD/NZD)
8>> South African Rand (ZAR)''')
print("")

#Now asking the user which currency they want to convert into INR
a = int(input("Enter the serial number of that currency you want to convert into INR :-"))
b = input("Enter the value :- ")
print("")


#Now creating the conditions
if a == 1:
    usd = float(b)*68.712272
    print(usd)
elif a == 2:
    eur = float(b)*77.3597946288
    print(eur)
elif a == 3:
    jpy = float(b)*0.63723
    print(jpy)
elif a == 4:
    gbp = float(b)*86.2017477681
    print(gbp)
elif a == 5:
    chf = float(b)*69.52850
    print(chf)
elif a == 6:
    cad = float(b)*52.45340
    print(cad)
elif a == 7:
    aud = float(b)*48.13280
    print(aud)
elif a == 8:
    zar = float(b)*4.90726
    print(zar)
else:
    print("Select from the above list only")
