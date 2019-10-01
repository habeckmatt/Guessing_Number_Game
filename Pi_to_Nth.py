import math

precision = int(input("How many spaces? "))

while precision > 50:
 	 print("Number to large")
 	 precision = int(input("How many spaces? "))
else:
     # The % makes the start of the specifier
     # '.'specifies precision
     # '*' the width is read from the next element in tuple
     print('%.*f' % (precision, math.pi))





