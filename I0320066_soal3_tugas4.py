#Berat_max = 50 lbs, 1 lbs = 0.45 kg
Berat_max = 50 * 0.45
print("Berat maksimum dalam kg adalah: ", Berat_max, "kg")

soalA = 110
soalB = 49

result1 = soalA < Berat_max
result2 = soalB < Berat_max
print("Jika berat maksimum adalah: ", Berat_max, 'kg', "maka dengan berat lebih dari 110 kg, hasilnya: ", result1)
print("Jika berat maksimum adalah: ", Berat_max, 'kg', "maka dengan berat 49 kg, hasilnya: ", result2)