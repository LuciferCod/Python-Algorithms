#python 3
#lucifer coder

#Palindrome checker

numbers = []
palindromechecker = []

#input
print("Enter integer without sign")
num = str(input("Enter number: "))

#manupilation

if len(num)!= 1:
    for i in num:
        numbers.append(i)
        palindromechecker.append(i)
    palindromechecker.reverse()
    if numbers == palindromechecker:
        output = "Palindrome"
    else:
        output = "Not Palindrome"
else:
    output = "Not Palindrome"

#output
print(output)
