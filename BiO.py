#Coded By EvCf1703
#Coded By Angga's
#Samlekom mamang :v
#Tools simple
#DONT RECODE 



print("\033[1;94m**********     **      ***********       [ Coded By Angga Surya Pardana ] ")
print("\033[1;94m*         *    **     *           *      [ https://github.com/EvCf1703] ")
print("\033[1;94m*         *    **     *           *      [ My Team D4RK SYST3M F41LUR3 S33K3R ] ")
print("\033[1;94m*         *    **     *           *  ")
print("\033[1;94m**********     **     *           * ")
print("\033[1;94m*         *    **     *           * ")
print("\033[1;94m*         *    **     *           * ")
print("\033[1;94m*         *    **     *           * ") 
print("\033[1;94m**********     **      *********** ")












































print(100*"=")
print"\033[91m*tolong isi dengan baik dan benar semua data-data anda!"
print" "
print" "
print" "
print" "
"clear"

print
nama_lengkap = raw_input("\033[93mNama Lengkap : ")
umur = raw_input("Umur : ")
jenis_kelamin = raw_input("Jenis Kelamin : ")
tempat_tanggal_lahir = raw_input("Tempat/tanggal lahir : ")
alamat = raw_input("Alamat : ")
agama = raw_input("Agama : ")
tinggi_badan = raw_input("Tinggi badan : ")
riwayat_penyakit = raw_input("Riwayat penyakit : ")
hobi = raw_input("Hobi : ")
sekolah = raw_input("Sekolah : ")
tlp = raw_input("Tlp : ")

teks = "\nNama Lengkap: {}\nUmur: {}\nJenis Kelamin: {}\nTempat/tanggal lahir: {}\nAlamat: {}\nAgama: {}\nTinggi badan: {}\nRiwayat penyakit: {}\nHobi: {}\nSekolah: {}\nTlp {}\n-----------------".format(nama_lengkap, umur, jenis_kelamin, tempat_tanggal_lahir, alamat, agama, tinggi_badan, riwayat_penyakit, hobi, sekolah, tlp)
file_bio = open("biodata.txt", "a")
file_bio.write(teks)
file_bio.close()
"clear"






























print"\033[91mNOTE: semua data anda telah dimasukan ke file 'biodata.txt'.\n terima kasih :)"
print
