#python 3
#luciferCoder
#fibonacci series

#input

Len = int(input("Enter Length of The Series: "))

# series

Fibonacci = [0,1,1]

for i in range(3,Len):
    int(i)
    Fibonacci.append(Fibonacci[i-1] + Fibonacci[i-2])

#output

print(Fibonacci)

