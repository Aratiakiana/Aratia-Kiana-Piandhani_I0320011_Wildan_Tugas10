print ("Program Biodata Diri")
print ("=================================")

# Mengambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
jenis_kelamin = input("Jenis kelamin: ")
agama = input("Agama: ")

# format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}\nJenis kelamin: {}\nAgama: {}".format(nama, umur, alamat, jenis_kelamin, agama)

# buka file untuk ditulis
file_bio = open("filebiodata.txt", "w")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()