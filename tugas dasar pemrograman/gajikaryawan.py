#input
print("========================================")
print("       Progam Hitung Gaji Karyawan      ")
print("========================================")

nama = input("Nama Karyawan : ")
golongan = input("Golongan Jabatan [1/2/3] : ")
pendidikan = input("Pendidikan [SMA/D1/D3/S1] : ")
jumlah_jamkerja = int(input("Jumlah Jam Kerja : "))
gaji_pokok = 300000

#Tunjangan Jabatan
if golongan == "1" :
    tunjanganjabatan = 0.05 * 300000
elif golongan == "2" :
    tunjanganjabatan = 0.1 * 300000
elif golongan == "3" :
    tunjanganjabatan = 0.15 * 300000
else :
    tunjanganjabatan = 0

#Tunjangan Pendidikan
if pendidikan == "SMA" or pendidikan == "sma":
    tunjanganpendidikan = 0.025 * 300000
elif pendidikan == "D1" or pendidikan == "d1":
    tunjanganpendidikan = 0.05 * 300000
elif pendidikan == "D3" or pendidikan == "d3":
    tunjanganpendidikan = 0.2 * 300000
elif pendidikan == "S1" or pendidikan == "s1":
    tunjanganpendidikan = 0.3 * 300000
else :
    tunjanganpendidikan = 0

#Honor Lembur
if jumlah_jamkerja >= 8 :
    honor_lembur = (jumlah_jamkerja - 8) * 3500
else :
    honor_lembur = 0

#Jumlah Tunjangan
tunjangan = tunjanganjabatan + tunjanganpendidikan

#Cetak Hasil
print("---------------------------------------------")
print("             Slip Gaji Karyawan              ")
print("---------------------------------------------")
print("Karyawan yang bernama    : ", str(nama))
print("Honor yang diterima")
print("    Gaji Pokok           : Rp", gaji_pokok)
print("    Tunjangan Jabatan    : Rp", str(tunjanganjabatan))
print("    Tunjangan Pendidikan : Rp", str(tunjanganpendidikan))
print("    Honor Lembur         : Rp", str(honor_lembur))
print("                         ________________ + ")
total_gaji = (gaji_pokok) + (tunjangan) + (honor_lembur)
print("Total Gaji               : Rp", str(total_gaji))
print("----------------------------------------------")