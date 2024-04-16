x="1234567"
print( x[1] )

x_len=len(x)
print(x_len)
#print(x[7]) error "string index out of range"

print(x)
print(x[0:len(x)-1:2])

print(x[0: len(x)-1 : -1])
print(x[::-1])
print(x[0:4])
print(x[0:4][::-1])