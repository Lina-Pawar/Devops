def Digits(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        #uses shorthand operator += for adding sum like sum=sum+int(digit)
    return sum
n= int(input(print("Enter an integer number: "))) #inputs an integer number
print("Sum of digits is",Digits(n)) #prints the sum