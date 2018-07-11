from bainsMaths import lucasNumber
isItPrime = int(input("Number to check: ")) #Get input number from user

lucas = lucasNumber((isItPrime-1)) #Get Lucas number
print("Lucas: "+ str(lucas) + ", To check: " + str(isItPrime)) #Print values (for debugging)
lucas = (lucas - 1) #Algo for chcking for prime numbers
prime = lucas%isItPrime
if prime == 0: #Final output
    print("Yes")
else:
    print("No")