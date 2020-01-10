print("\n\n\n\n\tTolong Masukkan Data Diri Anda Dengan Baik Dan Benar\n\n")

nama_lengkap = raw_input("Nama Lengkap : ")
jenis_kelamin = raw_input("Jenis Kelamin : ")
tempat_tanggal_lahir = raw_input("Tempat/tanggal lahir : ")
status = raw_input("Status : ")
alamat = raw_input("Alamat : ")
tlp = raw_input("Telp/Hp : ")
agama = raw_input("agama : ")
pendidikan = raw_input("Pendidikan : ")
kemampuan = raw_input("Kemampuan : ")
pengalaman_kerja = raw_input("Pengalaman Kerja : ")
personality = raw_input("Personality : ")
nama_ayah = raw_input("Nama Ayah : ")
nama_ibu = raw_input("Nama Ibu : ")
pekerjaan_ayah = raw_input("Pekerjaan Ayah : ")
pekerjaan_ibu = raw_input("Pekerjaan Ibu :")
alamat_orang_tua= raw_input("Alamat :")

teks = "\n----------------- {}\nNama Lengkap : {}\nJenis Kelamin : {}\nTempat/tanggal lahir : {}\nStatus : {}\nAlamat : {}\nTelepon/No Hp : {}\nAgama : {}\nPendidikan : {}\nKemampuan : {}\nPengalaman Kerja : {}\nPersonality : {}\n Nama Ayah : {}\n Nama Ibu : {}\n Pekerjaan Ayah : {}\n Pekerjaan Ibu : {}\n Alamat : {}\n-----------------".format(nama_lengkap, jenis_kelamin, tempat_tanggal_lahir, status, alamat, tlp, agama, pendidikan, kemampuan, pengalaman_kerja, personality, nama_ayah, nama_ibu, pekerjaan_ayah, pekerjaan_ibu, alamat_orang_tua)
file_bio = open("biodata.txt", "a")
file_bio.write(teks)
file_bio.close()

print("\n\tNote : Biodata sudah selesai file telah disimpan dengan nama biodata.txt\n")
print("\n\tTerimakasih")




