#4 adalah 100 dalam biner dan 11 adalah 1011

x = 4
y = 11

print("Nilai: ", x,", binarynya", format(x, '08b'))
print("Nilai: ", y,", binarynya", format(y, '08b'))

#a. 4 | 11
c = 4 | 11
print("===========(4 | 11)===========")
print("Nilai: ",x,", binarynya", format(x, '08b'))
print("Nilai: ",y,", binarynya", format(y, '08b'))
print("--------------------------------(|)")
print("Nilai ", c,", binarynya", format(c, '08b'))

#b. 4 >> 11
c = 4 >> 11
print("===========(4 >> 11)===========")
print("Nilai: ",x,", binarynya", format(x, '08b'))
print("Nilai: ",y,", binarynya", format(y, '08b'))
print("--------------------------------(>>)")
print("Nilai ", c,", binarynya", format(c, '08b'))

#c. 4 ^ 11
print("===========(4 ^ 11)===========")
print("Nilai: ",x,", binarynya", format(x, '08b'))
print("Nilai: ",y,", binarynya", format(y, '08b'))
print("--------------------------------(^)")
print("Nilai ", c,", binarynya", format(c, '08b'))

#d. ~4
c = ~4
print("===========(~4)===========")
print("Nilai: ",x,", binarynya", format(x, '08b'))
print("Nilai: ",y,", binarynya", format(y, '08b'))
print("--------------------------------(~)")
print("Nilai ", c,", binarynya", format(c, '08b'))

#e. 11 & 4
c = 11 & 4
print("===========(11 & 4)===========")
print("Nilai: ",x,", binarynya", format(x, '08b'))
print("Nilai: ",y,", binarynya", format(y, '08b'))
print("--------------------------------(&)")
print("Nilai ", c,", binarynya", format(c, '08b'))