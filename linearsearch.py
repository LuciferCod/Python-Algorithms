#python3

#linear search
#Lucifer Coder

#input

n = int(input("Enter number: "))
sortarray = [int(x) for x in input().split()]
#print(sortarray)

#manupilation

sortarray.sort()
#print(sortarray)

length = len(sortarray)
int(length)

for i in range(0,length + 1):
    if i == n:
         output = "number exists"
         break
    output = "number does not exist"

#output

print(output)

    

