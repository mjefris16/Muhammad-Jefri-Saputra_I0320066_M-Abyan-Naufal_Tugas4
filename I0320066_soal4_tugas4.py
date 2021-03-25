#Untuk mendaftar pada kursus online, calon siswa harus berusia minimal 21 tahun dan telah lulus ujian kualifikasi.

print("Berapa usia kamu?")
Usia = (input("Usia: "))
print("Apakah Anda sudah lulus ujian kualifikasi (Y / T)?")
Jawab = (input("Jawab: "))

if Usia >= '21':
    if Jawab == 'Y':
        print("Anda dapat mendaftar di kursus.")
    else:
        print("Anda tidak dapat mendaftar di kursus.")
else:
    print("Anda tidak dapat mendaftar di kursus.")