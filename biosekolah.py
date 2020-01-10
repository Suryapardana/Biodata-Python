
print("Tolong Masukkan Data Diri Anda Dengan Baik Dan Benar")

nama_lengkap = raw_input("Nama Lengkap : ")
nis = raw_input("NIS : ")
kelas = raw_input("Kelas : ")
tempat_tanggal_lahir = raw_input("Tempat/tanggal lahir : ")
agama = raw_input("Agama : ")
ayah = raw_input("Nama Ayah : ")
ibu = raw_input("Nama Ibu : ")
pekerjaan_ayah = raw_input("Pekerjaan Ayah: ")
pekerjaan_ibu = raw_input("Pekerjaan Ibu : ")
alamat = raw_input("Alamat : ")
tlp = raw_input("Tlp/hp : ")
motto = raw_input("Motto : ")
motivasi = raw_input("motivasi : ")
prestasi = raw_input("Prestasi : ")
hobi = raw_input("Hobbi : ")
kesan = raw_input("Kesan :")
pesan = raw_input("Pesan :")

teks = "\n----------------- {}\nNama Lengkap : {}\nNIS : {}\nKelas : {}\nTempat/tanggal lahir : {}\nAgama: {}\nNama Ayah : {}\nNama Ibu : {}\nPekerjaan Ayah : {}\nPekerjaan ibu: {}\nAlamat : {}\nTelp/Hp : {}\nMotto : {}\n Motivasi : {}\n Prestasi : {}\n Prestasi : {}\n Kesan : {}\n Pesan : {}\n-----------------".format(nama_lengkap, nis, kelas, tempat_tanggal_lahir, agama, ayah, ibu, pekerjaan_ayah, pekerjaan_ibu, alamat, tlp, motto, motivasi, prestasi, hobi, kesan, pesan)
file_bio = open("biodata.txt", "a")
file_bio.write(teks)
file_bio.close()

print("Note : Biodata sudah selesai file telah disimpan dengan nama biodata.txt\n")
print("Terimakasih")




