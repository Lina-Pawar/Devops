n=int(input(print("Enter a number=")))
lst=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'] #declaring a list with all corresponding words for digits
words=[]
s=""
if n==0:
    print(lst[0]) #checking if number is zero
else:
    while n>0:
        words.append(lst[n%10]) #adding the respective words from lst 
        n=n//10
    words.reverse() #reversing the list to make them in correct order
print(*words) #printing the list