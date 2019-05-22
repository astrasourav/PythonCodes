def my_fun(x, y):
    if x == "c":
        ans = (y-32) * 0.55
        return(ans)
    elif x == "f":
        ans = (y * 1.8) + 32
        return(ans)
    else:
        print("Incorrent parameters")

x = str.lower(input("f to convert to fahrenheit, c to convert to celcius"))
y = float(input("enter temp"))

ans = my_fun(x,y)
print(ans)
