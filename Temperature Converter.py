# In this project we will convert temperature to (Degrees) or (Celcius),and the input will be given by the user

 print("""This is Temperature Converter program.
 Hit enter to continue""")
 x=str.lower(input("To convert the Temperature to Fahrenheit type (F), for Celsius type (C)"))
 y=int(input("Enter the temperature here :-"))
 if x=="c":
    answer1=int((y-32)*(5/9))
    print(answer1)
 elif x=="f":
    answer2=int((y*1.8)+32)
    print(answer2)
 else:
    print("There is no input")
    
    
    
    
# Thank you :)
