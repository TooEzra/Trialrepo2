a = "1010" #10
b = "0101" #5

sum_decimal = int(a, 2) + int(b, 2)
sum_binary = bin(sum_decimal)

print("Sum in binary:", sum_binary)  #output : 0b1111